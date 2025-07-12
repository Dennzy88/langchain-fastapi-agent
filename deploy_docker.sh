#!/bin/bash

# 🚀 LangChain FastAPI Agent - Docker Deployment Script
# Automated Docker setup and deployment

set -e

echo "🐳 LangChain FastAPI Agent - Docker Deployment"
echo "=============================================="

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    echo "   Visit: https://docs.docker.com/get-docker/"
    exit 1
fi

# Check if Docker Compose is available
if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
    echo "❌ Docker Compose is not available. Please install Docker Compose."
    exit 1
fi

# Check for .env file
if [ ! -f ".env" ]; then
    echo "⚠️  .env file not found. Creating from template..."
    if [ -f ".env.example" ]; then
        cp .env.example .env
        echo "📝 Please edit .env file and add your OpenAI API key"
        echo "   OPENAI_API_KEY=sk-your-actual-api-key-here"
        exit 1
    else
        echo "❌ .env.example file not found. Please create .env manually."
        exit 1
    fi
fi

# Check if OPENAI_API_KEY is set
if ! grep -q "OPENAI_API_KEY=sk-" .env; then
    echo "⚠️  OpenAI API key not found in .env file"
    echo "   Please add: OPENAI_API_KEY=sk-your-actual-api-key-here"
    exit 1
fi

echo "🏗️  Building Docker image..."
if command -v docker-compose &> /dev/null; then
    docker-compose build
else
    docker compose build
fi

echo "🚀 Starting services..."
if command -v docker-compose &> /dev/null; then
    docker-compose up -d
else
    docker compose up -d
fi

echo ""
echo "✅ Deployment complete!"
echo ""
echo "🎯 API URL: http://localhost:8000"
echo "📖 Documentation: http://localhost:8000/docs"
echo "🏥 Health Check: http://localhost:8000/health"
echo ""
echo "📊 View logs: docker-compose logs -f langchain-agent"
echo "🛑 Stop services: docker-compose down"
echo ""

# Wait for service to be ready
echo "⏳ Waiting for service to be ready..."
for i in {1..30}; do
    if curl -s http://localhost:8000/health > /dev/null 2>&1; then
        echo "✅ Service is ready!"
        break
    fi
    echo "   Attempt $i/30..."
    sleep 2
done

# Test the API
echo ""
echo "🧪 Testing API..."
response=$(curl -s -X POST "http://localhost:8000/ask" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Hello! Are you working correctly?",
    "session_id": "docker-test"
  }' | python3 -m json.tool 2>/dev/null || echo "Failed to parse response")

if [[ $response == *"reply"* ]]; then
    echo "✅ API test successful!"
    echo "Response: $response"
else
    echo "⚠️  API test failed. Check logs: docker-compose logs langchain-agent"
fi

echo ""
echo "🎉 Your LangChain FastAPI Agent is now running in Docker!"
echo "   Visit http://localhost:8000/docs to start using the API"
