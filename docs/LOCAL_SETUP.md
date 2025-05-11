# Local Setup Guide for SysPulse

This guide will help you run SysPulse on your local machine without AWS deployment.

## Prerequisites

1. **Required Tools**
   - Python 3.8+
   - Docker and Docker Compose
   - Git

## Option 1: Using Docker (Recommended)

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/SysPulse.git
cd SysPulse
```

### 2. Start the Application
```bash
docker-compose up -d
```

### 3. Access the Dashboard
- Web Interface: http://localhost:8000
- API Documentation: http://localhost:8000/docs
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000

## Option 2: Manual Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/SysPulse.git
cd SysPulse
```

### 2. Create and Activate Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r src/requirements.txt
```

### 4. Run the Application
```bash
uvicorn syspulse.server:app --host 0.0.0.0 --port 8000
```

### 5. Access the Dashboard
- Web Interface: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   # Check if port 8000 is in use
   # On Windows
   netstat -ano | findstr :8000
   
   # On macOS/Linux
   lsof -i :8000
   ```

2. **Docker Issues**
   ```bash
   # Check Docker status
   docker ps
   
   # Check Docker logs
   docker-compose logs
   ```

3. **Python Environment Issues**
   ```bash
   # Verify Python version
   python --version
   
   # Verify pip installation
   pip list
   ```

### Solutions

1. **If port 8000 is in use:**
   - Stop the process using the port, or
   - Use a different port:
     ```bash
     uvicorn app:app --host 0.0.0.0 --port 8001
     ```

2. **If Docker containers fail to start:**
   ```bash
   # Remove existing containers
   docker-compose down
   
   # Rebuild and start
   docker-compose up -d --build
   ```

3. **If Python dependencies fail to install:**
   ```bash
   # Update pip
   python -m pip install --upgrade pip
   
   # Try installing dependencies again
   pip install -r src/requirements.txt
   ```

## Development

### Running Tests
```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests
pytest
```

### Code Style
```bash
# Install linting tools
pip install flake8

# Run linter
flake8 src/ --exclude=src/frontend,src/__pycache__ --max-line-length=120
```

## Support

If you encounter any issues:
1. Check the [Issues](https://github.com/yourusername/SysPulse/issues) page
2. Create a new issue with detailed information
3. Include relevant logs and error messages 