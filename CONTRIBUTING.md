# Contributing to OpenJobs

Thank you for your interest in contributing to OpenJobs! We welcome contributions from the community.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue on GitHub with:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected vs. actual behavior
- Your environment (OS, Python version, browser)
- Screenshots if applicable

### Suggesting Features

Feature requests are welcome! Please create an issue with:
- A clear description of the feature
- Use cases and benefits
- Any implementation ideas you have

### Pull Requests

1. **Fork the repository** and create your branch from `main`
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Set up your development environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Make your changes**
   - Write clean, readable code
   - Follow the existing code style
   - Add comments for complex logic
   - Update documentation as needed

4. **Test your changes**
   - Ensure the application runs without errors
   - Test all affected functionality
   - Check for any broken features

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: brief description of your changes"
   ```
   
   Use conventional commit messages:
   - `Add:` for new features
   - `Fix:` for bug fixes
   - `Update:` for updates to existing features
   - `Refactor:` for code refactoring
   - `Docs:` for documentation changes

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Provide a clear title and description
   - Reference any related issues
   - Wait for review and address any feedback

## Development Guidelines

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Keep functions focused and concise
- Add docstrings to functions and classes

### Database Changes

- Always create migrations for database changes
  ```bash
  flask db migrate -m "Description of changes"
  flask db upgrade
  ```
- Test migrations both up and down

### Frontend

- Keep HTML templates clean and semantic
- Use existing CSS classes when possible
- Ensure responsive design on mobile devices
- Test across different browsers

### Security

- Never commit sensitive data (API keys, passwords)
- Use environment variables for configuration
- Validate and sanitize all user inputs
- Follow Flask security best practices

## Questions?

If you have questions about contributing, feel free to:
- Open an issue for discussion
- Contact the maintainer at hamish@atech.industries

Thank you for contributing to OpenJobs!
