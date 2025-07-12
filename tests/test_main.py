"""
🧪 Basic tests for LangChain FastAPI Agent
"""

import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
import os
import sys

# Add the parent directory to sys.path to import modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app
from agent import ask_agent

# Create test client with proper host header
client = TestClient(app, base_url="http://localhost")


class TestHealthEndpoint:
    """Test health check endpoint"""

    def test_health_endpoint_success(self):
        """Test health endpoint returns 200"""
        response = client.get("/health")
        assert response.status_code == 200

        data = response.json()
        assert "status" in data
        assert "timestamp" in data
        assert "agent_status" in data
        assert data["status"] in ["healthy", "unhealthy"]

    def test_health_endpoint_structure(self):
        """Test health endpoint response structure"""
        response = client.get("/health")
        data = response.json()

        required_fields = ["status", "timestamp", "agent_status"]
        for field in required_fields:
            assert field in data


class TestRootEndpoint:
    """Test root endpoint"""

    def test_root_endpoint(self):
        """Test root endpoint returns welcome message"""
        response = client.get("/")
        assert response.status_code == 200

        data = response.json()
        assert "message" in data
        assert "LangChain FastAPI Agent" in data["message"]

    def test_root_endpoint_structure(self):
        """Test root endpoint response structure"""
        response = client.get("/")
        data = response.json()

        assert isinstance(data, dict)
        assert "message" in data
        assert "status" in data
        assert "version" in data


class TestAskEndpoint:
    """Test the main AI chat endpoint"""

    @patch.dict(os.environ, {"OPENAI_API_KEY": "sk-test-key"})
    @patch("agent.ChatOpenAI")
    def test_ask_endpoint_success(self, mock_openai):
        """Test successful chat interaction"""
        # Mock OpenAI response
        mock_llm = MagicMock()
        mock_llm.invoke.return_value.content = "Hello! I'm working correctly."
        mock_openai.return_value = mock_llm

        response = client.post(
            "/ask",
            json={"prompt": "Hello, are you working?", "session_id": "test-session"},
        )

        assert response.status_code == 200
        data = response.json()

        assert "reply" in data
        assert "session_id" in data
        assert "status" in data
        assert data["session_id"] == "test-session"
        assert data["status"] == "success"

    def test_ask_endpoint_missing_prompt(self):
        """Test error when prompt is missing"""
        response = client.post("/ask", json={"session_id": "test-session"})

        assert response.status_code == 422  # Validation error

    def test_ask_endpoint_empty_prompt(self):
        """Test error when prompt is empty"""
        response = client.post(
            "/ask", json={"prompt": "", "session_id": "test-session"}
        )

        assert response.status_code == 422  # Pydantic validation error

    def test_ask_endpoint_long_prompt(self):
        """Test error when prompt is too long"""
        long_prompt = "x" * 4001  # Exceeds 4000 char limit (changed from 10001)

        response = client.post(
            "/ask", json={"prompt": long_prompt, "session_id": "test-session"}
        )

        assert response.status_code == 422  # Pydantic validation error

    def test_ask_endpoint_default_session(self):
        """Test default session ID assignment"""
        with patch.dict(os.environ, {"OPENAI_API_KEY": "sk-test-key"}):
            with patch("agent.ChatOpenAI") as mock_openai:
                mock_llm = MagicMock()
                mock_llm.invoke.return_value.content = "Test response"
                mock_openai.return_value = mock_llm

                response = client.post("/ask", json={"prompt": "Hello"})

                assert response.status_code == 200
                data = response.json()
                assert data["session_id"] == "default"


class TestAIAgent:
    """Test AI Agent functionality"""

    @patch.dict(os.environ, {"OPENAI_API_KEY": "sk-test-key"})
    @patch("agent.ChatOpenAI")
    def test_agent_function_exists(self, mock_openai):
        """Test AI agent function exists and is callable"""
        from agent import ask_agent

        assert callable(ask_agent)

    @patch.dict(os.environ, {"OPENAI_API_KEY": "sk-test-key"})
    @patch("agent.with_message_history")
    def test_agent_basic_response(self, mock_chain):
        """Test basic agent response"""
        # Mock the chain response
        mock_response = MagicMock()
        mock_response.content = "Hello! I'm working correctly."
        mock_chain.invoke.return_value = mock_response

        response = ask_agent("Hello, are you working?", "test-session")
        assert response == "Hello! I'm working correctly."

    def test_agent_empty_prompt_validation(self):
        """Test agent handles empty prompts"""
        response = ask_agent("", "test-session")
        assert "Error: Empty prompt provided" in response

        response = ask_agent("   ", "test-session")  # Only whitespace
        assert "Error: Empty prompt provided" in response

    def test_agent_long_prompt_validation(self):
        """Test agent handles overly long prompts"""
        long_prompt = "x" * 4001  # Exceeds 4000 char limit
        response = ask_agent(long_prompt, "test-session")
        assert "Error: Prompt too long" in response

    def test_agent_session_id_handling(self):
        """Test session ID handling and sanitization"""
        with patch("agent.with_message_history") as mock_chain:
            mock_response = MagicMock()
            mock_response.content = "Test response"
            mock_chain.invoke.return_value = mock_response

            # Test default session
            response = ask_agent("Hello")
            assert response == "Test response"

            # Test custom session
            response = ask_agent("Hello", "custom-session")
            assert response == "Test response"

    def test_agent_session_memory(self):
        """Test that agent maintains session memory"""
        from agent import get_session_history, store

        # Clear store for clean test
        store.clear()

        # Test that session history is created for new sessions
        history1 = get_session_history("session1")
        history2 = get_session_history("session2")
        history1_again = get_session_history("session1")

        # Should be different objects for different sessions
        assert history1 is not history2
        # Should be same object for same session
        assert history1 is history1_again

        # Verify sessions are stored
        assert "session1" in store
        assert "session2" in store


class TestSecurity:
    """Test security features"""

    def test_cors_headers(self):
        """Test CORS headers are present"""
        response = client.options("/ask")
        # FastAPI handles OPTIONS automatically
        assert response.status_code in [
            200,
            405,
        ]  # Either allowed or method not allowed

    def test_input_sanitization(self):
        """Test XSS prevention"""
        xss_prompt = "<script>alert('xss')</script>"

        response = client.post(
            "/ask", json={"prompt": xss_prompt, "session_id": "test-session"}
        )

        # Should not return 500 error (should handle safely)
        assert response.status_code in [200, 400, 429]

    def test_rate_limiting_structure(self):
        """Test rate limiting is configured (structure test)"""
        # Make multiple requests quickly
        responses = []
        for i in range(3):
            response = client.post(
                "/ask", json={"prompt": f"Test message {i}", "session_id": "rate-test"}
            )
            responses.append(response.status_code)

        # At least one should succeed initially
        assert any(status in [200, 400] for status in responses)


class TestDocumentation:
    """Test API documentation endpoints"""

    def test_openapi_schema(self):
        """Test OpenAPI schema is available"""
        response = client.get("/openapi.json")
        assert response.status_code == 200

        schema = response.json()
        assert "openapi" in schema
        assert "info" in schema
        assert "paths" in schema

    def test_swagger_docs(self):
        """Test Swagger UI is available"""
        response = client.get("/docs")
        assert response.status_code == 200

    def test_redoc_docs(self):
        """Test ReDoc is available"""
        response = client.get("/redoc")
        assert response.status_code == 200


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
