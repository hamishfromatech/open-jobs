import os
from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError, Email
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_session import Session
from datetime import timedelta
from models import db, User, Job
from jobs import jobs

# Initialize extensions
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'admin_dashboard.login'
migrate = Migrate()

# Database Models


def create_app():
    """Factory function for creating the Flask application with modern configuration"""
    app = Flask(__name__)
    
    # Configuration
    app.config.update(
        SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL', 'sqlite:///openjobs.db'),
        SECRET_KEY=os.getenv('SECRET_KEY'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        TEMPLATES_AUTO_RELOAD=True,
        SQLALCHEMY_ENGINE_OPTIONS={
            'pool_pre_ping': True,
            'pool_recycle': 300,
            'pool_timeout': 20
        },
        SESSION_TYPE='filesystem',
        PERMANENT_SESSION_LIFETIME=timedelta(days=7),
        ADMIN_LOGIN_REQUIRED=True,
        WTF_CSRF_ENABLED=True,
        RATELIMIT_DEFAULT='100/hour'
    )

    # Initialize extensions with app
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # Configure session handling
    Session(app)

    # User loader callback
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    from jobs import jobs
    from admin import admin as admin_blueprint
    
    app.register_blueprint(jobs)
    app.register_blueprint(admin_blueprint)

    # Register CLI commands
    from cli import init_db_command, create_admin_command
    app.cli.add_command(init_db_command)
    app.cli.add_command(create_admin_command)

    # Register error handlers
    register_error_handlers(app)

    # Global template context
    @app.context_processor
    def inject_globals():
        from datetime import datetime
        return dict(
            current_user=current_user,
            now=datetime.now
        )

    return app

def register_error_handlers(app):
    """Register custom error handlers with modern error pages"""
    
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return render_template('errors/500.html'), 500

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Forms
    class RegisterForm(FlaskForm):
        name = StringField('Full Name', 
                          validators=[InputRequired(), Length(min=2, max=100)],
                          render_kw={"placeholder": "Full Name", 
                                    "class": "form-input"})
        username = StringField('Username', 
                              validators=[InputRequired(), Length(min=4, max=20)],
                              render_kw={"placeholder": "Username",
                                        "class": "form-input"})
        email = StringField('Email', 
                           validators=[InputRequired(), Email()],
                           render_kw={"placeholder": "Email",
                                     "class": "form-input"})
        password = PasswordField('Password',
                               validators=[InputRequired(), Length(min=8, max=20)],
                               render_kw={"placeholder": "Password",
                                         "class": "form-input"})
        submit = SubmitField("Register", render_kw={"class": "submit-btn"})

        def validate_username(self, username):
            existing_user_username = User.query.filter_by(username=username.data).first()
            if existing_user_username:
                raise ValidationError("That username already exists. Please choose a different one. ❌")
                
        def validate_email(self, email):
            existing_user_email = User.query.filter_by(email=email.data).first()
            if existing_user_email:
                raise ValidationError("That email is already registered. Please use a different one. ❌")

    class LoginForm(FlaskForm):
        username = StringField(validators=[InputRequired(), Length(min=4, max=20)],
                             render_kw={"placeholder": "Username",
                                       "class": "form-input"})
        password = PasswordField(validators=[InputRequired(), Length(min=8, max=20)],
                               render_kw={"placeholder": "Password",
                                         "class": "form-input"})
        submit = SubmitField("Login", render_kw={"class": "submit-btn"})

    # Routes
    @app.route('/')
    def index():
        # Check if any admin users exist
        admin_exists = User.query.filter_by(is_admin=True).first()
        if not admin_exists:
            return redirect(url_for('admin_setup'))

        # Get latest jobs for the homepage
        latest_jobs = Job.query.filter_by(
            status='active',
            is_deleted=False
        ).order_by(Job.created_at.desc()).limit(6).all()
        return render_template('index.html', latest_jobs=latest_jobs)

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        form = RegisterForm()
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data)
            new_user = User(
                name=form.name.data,
                username=form.username.data,
                email=form.email.data,
                password=hashed_password
            )
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        return render_template('register.html', form=form)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                flash('Welcome back!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid username or password. Please try again.', 'error')
        return render_template('login.html', form=form)

    @app.route('/logout', methods=['GET', 'POST'])
    @login_required
    def logout():
        # Clear admin session if user is admin
        if current_user.is_admin and session.get('admin_authenticated'):
            session.pop('admin_authenticated', None)

        logout_user()
        flash('You have been logged out successfully.', 'success')
        return redirect(url_for('index'))

    @app.route('/dashboard')
    @login_required
    def dashboard():
        # Get user's posted jobs
        user_jobs = Job.query.filter_by(user_id=current_user.id).order_by(Job.created_at.desc()).all()
        return render_template('dashboard.html', name=current_user.username, jobs=user_jobs)

    @app.route('/admin-setup', methods=['GET', 'POST'])
    def admin_setup():
        # Check if admin already exists
        admin_exists = User.query.filter_by(is_admin=True).first()
        if admin_exists:
            return redirect(url_for('index'))

        form = RegisterForm()
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data)
            admin_user = User(
                name=form.name.data,
                username=form.username.data,
                email=form.email.data,
                password=hashed_password,
                is_admin=True,
                is_active=True
            )
            db.session.add(admin_user)
            db.session.commit()
            flash('Admin user created successfully! Please log in.', 'success')
            return redirect(url_for('login'))
        return render_template('admin_setup.html', form=form)

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True, port=6758)
