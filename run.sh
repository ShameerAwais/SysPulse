#!/bin/bash

echo "🚀 Starting SysPulse deployment..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first:"
    echo "Visit: https://docs.docker.com/get-docker/"
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first:"
    echo "Visit: https://docs.docker.com/compose/install/"
    exit 1
fi

# Pull the latest changes if it's a git repository
if [ -d .git ]; then
    echo "📥 Pulling latest changes..."
    git pull
fi

# Start the application
echo "🚀 Starting SysPulse..."
docker-compose up -d

echo "
✅ SysPulse is now running! You can access:

📊 Dashboard: http://localhost:8000
📚 API Documentation: http://localhost:8000/docs
📈 Prometheus: http://localhost:9090
🎨 Grafana: http://localhost:3000

To stop SysPulse, run: docker-compose down
" 