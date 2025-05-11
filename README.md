# SysPulse - System Monitoring Dashboard

A modern, real-time system monitoring dashboard built with FastAPI, Docker, Prometheus, and Grafana. Monitor your system's CPU, memory, disk usage, and more with a beautiful, responsive interface.

![SysPulse Dashboard](image.png)

## Features

- 📊 Real-time system metrics monitoring
- 💻 CPU usage and performance tracking
- 🧠 Memory utilization and availability
- 💾 Disk space monitoring
- 🌐 Network statistics
- ⚡ Fast and responsive UI
- 🔄 Auto-refreshing metrics
- 🐳 Docker containerization
- 📈 Prometheus metrics integration
- 🎨 Grafana visualization support
- 🔔 Custom alert notifications
- 📱 Mobile-responsive design

---

# 1. Running Locally (Manual Python Setup)

### Prerequisites
- Python 3.8+
- Git

### Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/ShameerAwais/SysPulse.git
   cd SysPulse
   ```
2. **Create and activate a virtual environment:**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   # On macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r src/requirements.txt
   ```
4. **Run the application:**
   ```bash
   uvicorn syspulse.server:app --host 0.0.0.0 --port 8000
   ```
5. **Access the dashboard:**
   - Web Interface: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

---

# 2. Deployment through Docker (Recommended)

### Prerequisites
- Docker Desktop (includes Docker and Docker Compose)
  - [Download for Windows](https://docs.docker.com/desktop/install/windows-install/)
  - [Download for Mac](https://docs.docker.com/desktop/install/mac-install/)
  - [Download for Linux](https://docs.docker.com/desktop/install/linux-install/)

### Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/ShameerAwais/SysPulse.git
   cd SysPulse
   ```
2. **Run the application:**
   - On Windows: Double-click `run.bat` or run it in PowerShell
   - On Mac/Linux: Run `./run.sh` in terminal

   *Alternatively, you can use Docker Compose directly:*
   ```bash
   docker-compose up -d
   ```
3. **Access the dashboard:**
   - Web Interface: http://localhost:8000
   - API Documentation: http://localhost:8000/docs
   - Prometheus: http://localhost:9090
   - Grafana: http://localhost:3000

4. **Stopping SysPulse:**
   ```bash
   docker-compose down
   ```

---

# 3. Deployment through AWS

SysPulse can be deployed on AWS for production or cloud use. For a full guide, see [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md).

### Typical Steps
1. **Provision AWS infrastructure** (using Terraform or AWS Console)
2. **Build and push Docker images** (to ECR or another registry)
3. **Launch EC2 instances or ECS services**
4. **Configure security groups, networking, and monitoring**
5. **Access the dashboard using your AWS public IP or domain**

*See the deployment guide for detailed, step-by-step instructions, including security and troubleshooting tips.*

---

## API Endpoints

- `GET /api/health` - Health check endpoint
- `GET /api/metrics/cpu` - CPU metrics
- `GET /api/metrics/memory` - Memory usage statistics
- `GET /api/metrics/disk` - Disk space information

## Project Structure

```
SysPulse/
├── syspulse/               # Main application (advanced dashboard)
│   ├── server.py           # FastAPI app entry point
│   ├── static/             # Frontend static files
│   └── templates/          # Jinja2 HTML templates
├── src/
│   └── requirements.txt    # Python dependencies
├── run.sh                  # Quick start script (Linux/Mac)
├── run.bat                 # Quick start script (Windows)
├── docker-compose.yml      # Docker Compose configuration
├── Dockerfile              # Docker build file
└── README.md               # Project documentation
```

## Development

1. Install development dependencies:
   ```bash
   pip install -r src/requirements-dev.txt
   ```
2. Run tests:
   ```bash
   pytest
   ```
3. Run linting:
   ```bash
   flake8 src/ --exclude=src/frontend,src/__pycache__ --max-line-length=120
   ```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions, please:
1. Check the [Issues](https://github.com/yourusername/SysPulse/issues) page
2. Create a new issue if your problem isn't already listed

---

Enjoy monitoring with SysPulse! 🚀
