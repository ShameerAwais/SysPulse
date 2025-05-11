@echo off
echo 🚀 Starting SysPulse deployment...

REM Check if Docker is installed
where docker >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo ❌ Docker is not installed. Please install Docker first:
    echo Visit: https://docs.docker.com/get-docker/
    exit /b 1
)

REM Check if Docker Compose is installed
where docker-compose >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo ❌ Docker Compose is not installed. Please install Docker Compose first:
    echo Visit: https://docs.docker.com/compose/install/
    exit /b 1
)

REM Pull the latest changes if it's a git repository
if exist .git (
    echo 📥 Pulling latest changes...
    git pull
)

REM Start the application
echo 🚀 Starting SysPulse...
docker-compose up -d

echo.
echo ✅ SysPulse is now running! You can access:
echo.
echo 📊 Dashboard: http://localhost:8000
echo 📚 API Documentation: http://localhost:8000/docs
echo 📈 Prometheus: http://localhost:9090
echo 🎨 Grafana: http://localhost:3000
echo.
echo To stop SysPulse, run: docker-compose down 