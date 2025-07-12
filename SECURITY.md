# Security Configuration Guide

## Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `API_KEY`: Optional API key for protecting your service endpoints
- `ENVIRONMENT`: Set to 'production' in production
- `LOG_LEVEL`: Logging level (DEBUG, INFO, WARNING, ERROR)

## Security Features Implemented

### 1. Input Validation
- Prompt length limits (max 4000 characters)
- Session ID validation (alphanumeric only)
- Empty input rejection

### 2. Rate Limiting
- 10 requests per minute per IP address
- Configurable limits

### 3. CORS Protection
- Controlled origins for web applications
- Secure headers

### 4. API Key Authentication (Optional)
- Set `API_KEY` environment variable to enable
- Include in Authorization header: `Bearer your-api-key`

### 5. Request Logging
- All requests are logged with IP and session info
- Error tracking

### 6. Error Handling
- Secure error messages (no sensitive data exposure)
- Proper HTTP status codes

## Production Recommendations

1. **Use HTTPS**: Always run behind a reverse proxy with SSL/TLS
2. **Rate Limiting**: Implement Redis-based rate limiting for multi-instance deployments
3. **Monitoring**: Add monitoring and alerting
4. **API Key**: Enable API key authentication in production
5. **Firewall**: Restrict access to known IP ranges if possible
6. **Logging**: Use structured logging and log aggregation

## Example Usage

```bash
# Without API key
curl -X POST "http://localhost:8000/ask" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Hello!", "session_id": "user123"}'

# With API key
curl -X POST "http://localhost:8000/ask" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-api-key" \
  -d '{"prompt": "Hello!", "session_id": "user123"}'
```

API_KEY=moj-tajni-kljuc-123
