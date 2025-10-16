import click
from flask.cli import with_appcontext
from models import db, User
from app import create_app, bcrypt

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Initialize the database with modern schema."""
    app = create_app()
    with app.app_context():
        # Drop all tables first to ensure clean state
        db.drop_all()
        # Create all tables with new schema
        db.create_all()
        click.echo('✨ Database initialized successfully with modern schema!')

@click.command('create-admin')
@click.option('--username', prompt=True, help='Admin username')
@click.option('--email', prompt=True, help='Admin email')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='Admin password')
def create_admin_command(username, email, password):
    """Create an admin user with enhanced privileges."""
    app = create_app()
    with app.app_context():
        # Check if admin already exists
        if User.query.filter_by(is_admin=True).first():
            click.echo('❌ An admin user already exists!')
            return

        # Create admin user with modern details
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        admin = User(
            username=username,
            email=email,
            password=hashed_password,
            is_admin=True,
            name='Admin User',
            is_active=True
        )

        try:
            db.session.add(admin)
            db.session.commit()
            click.echo('✨ Admin user created successfully with premium access!')
        except Exception as e:
            db.session.rollback()
            click.echo(f'❌ Error creating admin user: {str(e)}')
