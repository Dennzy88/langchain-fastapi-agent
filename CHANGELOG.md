# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-07-12

### Added
- Initial release of LangChain FastAPI Agent
- FastAPI REST API with `/ask` endpoint
- GPT-4 integration via LangChain
- Session-based conversation memory system
- Comprehensive security features:
  - Input validation and sanitization
  - Rate limiting (10 requests/minute per IP)
  - CORS protection
  - Optional API key authentication
  - Secure error handling
- Complete documentation suite:
  - Detailed setup instructions (`UPUTSTVO.md`)
  - Quick reference guide (`QUICK_REF.md`)
  - Troubleshooting guide (`TROUBLESHOOTING.md`)
  - Security guidelines (`SECURITY.md`)
  - Git workflow documentation (`GIT_PODSETNIK.md`)
- Automated scripts:
  - Application startup (`start.sh`)
  - Security checker (`security_check.sh`)
  - Commit helper (`commit_helper.sh`)
- Health check endpoints
- Production-ready configuration
- Comprehensive `.gitignore` for security
- MIT License

### Security
- API keys protected with `.gitignore`
- Automated security scanning before git commits
- Input validation and length limits
- Rate limiting protection
- CORS policy enforcement
- Secure environment variable handling

### Documentation
- Complete API documentation
- Step-by-step setup guide
- Architecture diagrams
- Use case examples
- Troubleshooting procedures
- Security best practices
