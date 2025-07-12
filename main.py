from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, Field, validator
from agent import ask_agent
from dotenv import load_dotenv
import os
import time
import logging
from typing import Optional

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="LangChain FastAPI Agent",
    version="1.0.0",
    description="Secure AI Agent API with conversation memory",
)

# Security middleware
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["localhost", "127.0.0.1", "*.vercel.app", "testserver"],
)

# CORS middleware for web applications
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:8000",
    ],  # Add your frontend URLs
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Optional API key authentication
security = HTTPBearer(auto_error=False)
API_KEY = os.getenv("API_KEY")  # Optional API key for your service


class Prompt(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=4000, description="User message")
    session_id: str = Field(
        default="default", max_length=50, description="Session identifier"
    )

    @validator("prompt")
    def validate_prompt(cls, v):
        if not v.strip():
            raise ValueError("Prompt cannot be empty")
        return v.strip()

    @validator("session_id")
    def validate_session_id(cls, v):
        # Allow only alphanumeric and basic characters
        if not v.replace("-", "").replace("_", "").isalnum():
            raise ValueError(
                "Session ID can only contain letters, numbers, hyphens, and underscores"
            )
        return v


# Rate limiting storage (in production, use Redis)
request_times = {}


def rate_limit_check(request: Request):
    """Simple rate limiting: max 10 requests per minute per IP"""
    client_ip = request.client.host
    current_time = time.time()

    if client_ip not in request_times:
        request_times[client_ip] = []

    # Remove old requests (older than 1 minute)
    request_times[client_ip] = [
        req_time
        for req_time in request_times[client_ip]
        if current_time - req_time < 60
    ]

    # Check if too many requests
    if len(request_times[client_ip]) >= 10:
        raise HTTPException(status_code=429, detail="Too many requests")

    # Add current request
    request_times[client_ip].append(current_time)


async def verify_api_key(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Optional API key verification"""
    if API_KEY and credentials:
        if credentials.credentials != API_KEY:
            raise HTTPException(status_code=401, detail="Invalid API key")
    return credentials


@app.post("/ask")
async def ask(
    prompt: Prompt,
    request: Request,
    credentials: HTTPAuthorizationCredentials = Depends(verify_api_key),
):
    """
    Send a message to the AI agent
    """
    try:
        # Rate limiting
        rate_limit_check(request)

        logger.info(
            f"Request from {request.client.host} for session {prompt.session_id}"
        )

        # Call the agent
        response = ask_agent(prompt.prompt, prompt.session_id)

        return {"reply": response, "session_id": prompt.session_id, "status": "success"}

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "message": "LangChain FastAPI Agent is running!",
        "status": "healthy",
        "version": "1.0.0",
    }


@app.get("/health")
async def health_check():
    """Detailed health check"""
    try:
        # Test agent functionality
        test_response = ask_agent("test", "health_check")
        return {
            "status": "healthy",
            "agent_status": (
                "working"
                if "test" not in test_response.lower()
                or "error" not in test_response.lower()
                else "error"
            ),
            "timestamp": time.time(),
        }
    except Exception as e:
        return {"status": "unhealthy", "error": str(e), "timestamp": time.time()}
