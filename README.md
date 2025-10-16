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
git clone https://github.com/hamishfromatech/openjobs.git
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

4. Initialize the database:
```bash
flask db init
flask db migrate
flask db upgrade
```

5. Run the development server:
```bash
flask run
```

The application will be available at `http://localhost:5000`

## Project Structure

```
openjobs/
├── app.py              # Application entry point
├── models.py           # Database models (User, Job)
├── requirements.txt    # Project dependencies
├── static/            # Static files
│   ├── css/          # Stylesheets
│   └── js/           # JavaScript files
└── templates/         # HTML templates
    ├── base.html     # Base template
    ├── index.html    # Landing page
    ├── login.html    # Login page
    ├── register.html # Registration page
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

## Support

- **Documentation**: Check the `/docs` folder for detailed setup and customization guides
- **Issues**: Report bugs or request features on the GitHub Issues page
- **Discussions**: Join the community discussions for help and ideas

## Acknowledgments

- The open-source community for their invaluable tools and libraries
- [Flask](https://flask.palletsprojects.com/) and the Flask ecosystem
- [Unsplash](https://unsplash.com) for the beautiful images


## DONE FOR YOU
If you need help or want your own version of this, please contact me at hamish@atech.industries