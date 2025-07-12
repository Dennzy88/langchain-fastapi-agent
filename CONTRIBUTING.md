# Contributing to LangChain FastAPI Agent

First off, thank you for considering contributing to this project! 🎉

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)
- [Security Guidelines](#security-guidelines)

## Code of Conduct

This project and everyone participating in it is governed by our commitment to creating a welcoming, respectful, and harassment-free environment for everyone.

## How Can I Contribute?

### 🐛 Reporting Bugs

Before creating bug reports, please check the [troubleshooting guide](./TROUBLESHOOTING.md) as you might find that you don't need to create one.

**When filing a bug report, please include:**
- A clear and descriptive title
- Steps to reproduce the issue
- Expected vs actual behavior
- Your environment details (OS, Python version, etc.)
- Relevant log output

### 💡 Suggesting Enhancements

Enhancement suggestions are welcome! Please provide:
- A clear and descriptive title
- A detailed description of the proposed enhancement
- Explanation of why this enhancement would be useful
- Examples of how it would work

### 🔧 Code Contributions

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Follow our security guidelines
5. Add tests if applicable
6. Update documentation
7. Commit your changes
8. Push to your branch
9. Open a Pull Request

## Development Setup

```bash
# 1. Fork and clone the repository
git clone https://github.com/your-username/langchain-fastapi-agent.git
cd langchain-fastapi-agent

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Add your OpenAI API key to .env

# 5. Run tests (when available)
# python -m pytest

# 6. Start development server
./start.sh
```

## Pull Request Process

1. **Security First**: Always run `./security_check.sh` before committing
2. **Update Documentation**: Update relevant documentation for any changes
3. **Test Your Changes**: Ensure your changes work as expected
4. **Follow Git Workflow**: Use our secure commit process:
   ```bash
   git add .
   ./security_check.sh
   git commit -m "feat: your descriptive commit message"
   ```
5. **Clear PR Description**: Explain what your changes do and why

### Commit Message Format

We follow conventional commits:
- `feat:` - New features
- `fix:` - Bug fixes
- `docs:` - Documentation changes
- `style:` - Code style changes
- `refactor:` - Code refactoring
- `test:` - Adding tests
- `chore:` - Maintenance tasks

## Style Guidelines

### Python Code Style
- Follow PEP 8
- Use meaningful variable and function names
- Add docstrings for functions and classes
- Keep functions focused and small
- Use type hints where appropriate

### Documentation Style
- Use clear, concise language
- Include code examples where helpful
- Update relevant documentation files
- Follow existing documentation structure

### API Design
- RESTful principles
- Consistent response formats
- Proper HTTP status codes
- Clear error messages

## Security Guidelines

**🚨 CRITICAL**: Never commit API keys or sensitive data!

1. **Always run security checks**:
   ```bash
   ./security_check.sh
   ```

2. **Environment Variables**: Use `.env` file for secrets (it's gitignored)

3. **Input Validation**: Validate all user inputs

4. **Error Handling**: Don't expose sensitive information in errors

5. **Dependencies**: Keep dependencies updated

## Testing

When adding new features:
- Add appropriate tests
- Ensure existing tests pass
- Test edge cases
- Test security aspects

## Documentation Updates

For any changes, update:
- `README.md` if changing core functionality
- `UPUTSTVO.md` for setup/usage changes
- `TROUBLESHOOTING.md` for new known issues
- `SECURITY.md` for security-related changes
- `CHANGELOG.md` for all changes

## Questions?

- Check existing [documentation](./DOCS_INDEX.md)
- Look at [troubleshooting guide](./TROUBLESHOOTING.md)
- Open an issue for discussion

Thank you for contributing! 🚀
