# OpenJobs - Modern Job Board Platform

OpenJobs is a modern, open-source job board platform designed to connect professionals with top companies worldwide. The platform provides a solid foundation for building job marketplaces, career platforms, or recruitment websites with modern web technologies.

![OpenJobs Platform](https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&q=80)

## Features

- **Job Listings Management**: Post, edit, and manage job opportunities
- **User Authentication**: Secure registration, login, and session management
- **User Profiles**: Manage user accounts and job postings
- **Admin Dashboard**: Administrative interface for platform management
- **Responsive Design**: Modern UI with glassmorphism effects and gradients
- **Database Management**: SQLite with migration support for easy deployment

## Tech Stack

- **Backend**: Python with Flask
- **Database**: SQLite (easily configurable for PostgreSQL, MySQL, etc.)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Authentication**: Flask-Login with password hashing
- **Forms**: Flask-WTF with CSRF protection
- **Admin Panel**: Flask-Admin
- **Database Migrations**: Flask-Migrate

## Installation

1. Clone the repository:
```bash
git clone https://github.com/hamishfromatech/open-jobs.git
cd openjobs
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and set your SECRET_KEY and other configuration
```

5. Initialize the database:
```bash
flask db upgrade
```

6. Run the development server:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Project Structure

```
openjobs/
├── app.py              # Application entry point and factory
├── models.py           # Database models (User, Job)
├── admin.py            # Admin panel routes and views
├── jobs.py             # Job-related routes
├── forms.py            # WTForms definitions
├── cli.py              # CLI commands for database initialization
├── requirements.txt    # Project dependencies
├── .env.example        # Environment variable template
├── .gitignore          # Git ignore rules
├── LICENSE             # MIT License
├── migrations/         # Database migrations
├── static/             # Static files
│   ├── css/           # Stylesheets
│   └── js/            # JavaScript files
└── templates/          # HTML templates
    ├── admin/         # Admin panel templates
    ├── jobs/          # Job-related templates
    ├── errors/        # Error pages (404, 500)
    ├── base.html      # Base template
    ├── index.html     # Landing page
    ├── login.html     # Login page
    ├── register.html  # Registration page
    └── dashboard.html # User dashboard
```

## Customization

OpenJobs is designed as a starter template that you can easily customize:

- **Database**: Change `SQLALCHEMY_DATABASE_URI` in `app.py` to use PostgreSQL, MySQL, or other databases
- **Styling**: Modify CSS files in `static/css/` for your brand colors and design
- **Features**: Add new models, routes, and functionality as needed
- **Deployment**: Configure for production deployment on Heroku, AWS, or other platforms

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Environment Variables

The application requires the following environment variables:

- **SECRET_KEY**: Required for session management and CSRF protection. Generate using:
  ```bash
  python -c "import secrets; print(secrets.token_hex(32))"
  ```
- **DATABASE_URL**: Database connection string (defaults to SQLite)

See `.env.example` for a complete list of configuration options.

## First Run Setup

On first run, the application will prompt you to create an admin account at `/admin-setup`. This is required before accessing the admin dashboard.

## Support

- **Issues**: Report bugs or request features on the GitHub Issues page
- **Contact**: For custom implementations, contact hamish@atech.industries

## Acknowledgments

- The open-source community for their invaluable tools and libraries
- [Flask](https://flask.palletsprojects.com/) and the Flask ecosystem
- [Unsplash](https://unsplash.com) for the beautiful images


## DONE FOR YOU
If you need help or want your own version of this, please contact me at hamish@atech.industries