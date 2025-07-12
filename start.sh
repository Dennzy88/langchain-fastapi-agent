#!/bin/bash
# Start script za LangChain FastAPI Agent

echo "🚀 Pokretam LangChain FastAPI Agent..."
echo "📍 Lokacija: /Users/dennzy/langchain_fastapi_agent"
echo "🌐 URL: http://localhost:8000"
echo "📖 Docs: http://localhost:8000/docs"
echo ""

cd /Users/dennzy/langchain_fastapi_agent
/Users/dennzy/langchain_fastapi_agent/venv/bin/python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
