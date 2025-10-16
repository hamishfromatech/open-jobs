# Deployment Guide

This guide will help you deploy OpenJobs to production.

## Pre-Deployment Checklist

### Security
- [ ] Set a strong `SECRET_KEY` environment variable
- [ ] Never commit `.env` file to version control
- [ ] Review and update all environment variables
- [ ] Ensure DEBUG mode is disabled in production
- [ ] Configure secure database (PostgreSQL recommended)
- [ ] Enable HTTPS/SSL
- [ ] Review SECURITY.md guidelines

### Database
- [ ] Set up production database (PostgreSQL/MySQL recommended)
- [ ] Update `DATABASE_URL` environment variable
- [ ] Run database migrations: `flask db upgrade`
- [ ] Set up database backups
- [ ] Configure connection pooling

### Application
- [ ] Set `FLASK_ENV=production`
- [ ] Configure session storage (Redis recommended for production)
- [ ] Set up logging
- [ ] Configure error monitoring (e.g., Sentry)
- [ ] Test all functionality in staging environment

## Deployment Options

### Option 1: Heroku

1. Install Heroku CLI and login:
```bash
heroku login
```

2. Create a new Heroku app:
```bash
heroku create your-app-name
```

3. Add PostgreSQL:
```bash
heroku addons:create heroku-postgresql:mini
```

4. Set environment variables:
```bash
heroku config:set SECRET_KEY=your-secret-key
heroku config:set FLASK_ENV=production
```

5. Create a `Procfile`:
```
web: gunicorn app:app
```

6. Add gunicorn to requirements.txt:
```bash
echo "gunicorn>=20.1.0" >> requirements.txt
```

7. Deploy:
```bash
git push heroku main
```

8. Run migrations:
```bash
heroku run flask db upgrade
```

### Option 2: Railway

1. Install Railway CLI:
```bash
npm install -g @railway/cli
```

2. Login and initialize:
```bash
railway login
railway init
```

3. Add PostgreSQL:
```bash
railway add
# Select PostgreSQL
```

4. Set environment variables via Railway dashboard

5. Deploy:
```bash
railway up
```

### Option 3: DigitalOcean App Platform

1. Connect your GitHub repository
2. Configure environment variables in dashboard
3. Set build command: `pip install -r requirements.txt`
4. Set run command: `gunicorn app:app`
5. Deploy

### Option 4: AWS / VPS (Manual)

1. Set up Ubuntu server
2. Install dependencies:
```bash
sudo apt update
sudo apt install python3-pip python3-venv nginx
```

3. Clone repository and set up virtual environment:
```bash
git clone your-repo
cd openjobs
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn
```

4. Set up environment variables in `.env`

5. Configure Nginx as reverse proxy

6. Set up systemd service for gunicorn

7. Run migrations:
```bash
flask db upgrade
```

## Post-Deployment

- [ ] Create admin user via `/admin-setup`
- [ ] Test all functionality
- [ ] Monitor application logs
- [ ] Set up regular database backups
- [ ] Configure monitoring/alerting
- [ ] Update DNS records if needed

## Environment Variables Reference

Required:
- `SECRET_KEY`: Session encryption key
- `DATABASE_URL`: Database connection string

Optional:
- `FLASK_ENV`: Set to 'production'
- `FLASK_DEBUG`: Set to 'False'

## Monitoring

Consider setting up:
- Application monitoring (New Relic, Datadog)
- Error tracking (Sentry)
- Uptime monitoring (Pingdom, UptimeRobot)
- Log aggregation (Papertrail, Loggly)

## Maintenance

### Updating Dependencies
```bash
pip install --upgrade -r requirements.txt
```

### Database Backups
Set up automated daily backups of your database.

### Scaling
- Consider using Redis for session storage
- Implement caching for frequently accessed data
- Use CDN for static assets
- Scale horizontally with load balancer

## Troubleshooting

### Common Issues

**Database connection errors:**
- Verify DATABASE_URL is correct
- Check database credentials
- Ensure database is accessible

**Static files not loading:**
- Configure static file serving
- Use CDN or object storage for production

**Session issues:**
- Verify SECRET_KEY is set
- Check session configuration

## Support

For deployment assistance: hamish@atech.industries
