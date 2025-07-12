"""
Test configuration and fixtures
"""

import pytest
import os
from unittest.mock import patch


@pytest.fixture
def mock_openai_key():
    """Fixture to mock OpenAI API key"""
    with patch.dict(os.environ, {"OPENAI_API_KEY": "sk-test-key-for-testing"}):
        yield


@pytest.fixture
def test_session_id():
    """Fixture for test session ID"""
    return "test-session-12345"


@pytest.fixture
def sample_prompts():
    """Fixture with sample prompts for testing"""
    return {
        "simple": "Hello, how are you?",
        "complex": "Explain quantum computing in simple terms with examples.",
        "empty": "",
        "long": "x" * 10001,  # Exceeds limit
        "xss": "<script>alert('xss')</script>",
        "sql_injection": "'; DROP TABLE users; --",
    }
