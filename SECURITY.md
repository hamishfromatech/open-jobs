# Security Policy

## Supported Versions

Currently supported versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.x     | :white_check_mark: |

## Reporting a Vulnerability

We take the security of OpenJobs seriously. If you discover a security vulnerability, please follow these steps:

1. **Do NOT** open a public issue
2. Email security details to: hamish@atech.industries
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

You should receive a response within 48 hours. We'll work with you to understand and address the issue promptly.

## Security Best Practices

When deploying OpenJobs:

### Environment Variables
- **Never commit** `.env` files to version control
- Use strong, randomly generated `SECRET_KEY`
- Rotate secrets regularly

### Database
- Use strong passwords for production databases
- Enable SSL/TLS for database connections
- Regular backups

### Deployment
- Use HTTPS in production
- Keep dependencies updated
- Enable CSRF protection (enabled by default)
- Use secure session cookies
- Implement rate limiting

### User Data
- Passwords are hashed using Bcrypt
- Validate all user inputs
- Sanitize data before rendering
- Use parameterized queries (SQLAlchemy handles this)

## Known Security Considerations

- Default SQLite database is suitable for development only
- Admin routes require authentication
- CSRF protection is enabled via Flask-WTF
- Session management via Flask-Session

## Updates

Check regularly for dependency updates:
```bash
pip list --outdated
```

Update dependencies:
```bash
pip install --upgrade -r requirements.txt
```

## Contact

For security concerns: hamish@atech.industries
