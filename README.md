# SysPulse - System Monitoring Dashboard

A modern, real-time system monitoring dashboard built with FastAPI, Docker, Prometheus, and Grafana. Monitor your system's CPU, memory, disk usage, and more with a beautiful, responsive interface.

![SysPulse Dashboard](docs/images/dashboard.png)

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

## Quick Start (One-Command Deployment)

### Prerequisites
- Docker Desktop (includes Docker and Docker Compose)
  - [Download for Windows](https://docs.docker.com/desktop/install/windows-install/)
  - [Download for Mac](https://docs.docker.com/desktop/install/mac-install/)
  - [Download for Linux](https://docs.docker.com/desktop/install/linux-install/)

### Running SysPulse

1. Clone the repository:
```bash
git clone https://github.com/yourusername/SysPulse.git
cd SysPulse
```

2. Run the application:
- On Windows: Double-click `run.bat` or run it in PowerShell
- On Mac/Linux: Run `./run.sh` in terminal

That's it! SysPulse will automatically:
- Check for required dependencies
- Pull the latest changes
- Start all services
- Display access URLs

### Accessing SysPulse
Once running, you can access:
- 📊 Dashboard: http://localhost:8000
- 📚 API Documentation: http://localhost:8000/docs
- 📈 Prometheus: http://localhost:9090
- 🎨 Grafana: http://localhost:3000

### Stopping SysPulse
To stop the application, run:
```bash
docker-compose down
```

## AWS Deployment

For deploying SysPulse on AWS, please refer to our [Deployment Guide](docs/DEPLOYMENT.md) which includes:
- AWS infrastructure setup
- Terraform configuration
- Security considerations
- Troubleshooting steps
- Maintenance procedures

## Manual Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r src/requirements.txt
```

3. Run the application:
```bash
cd src
uvicorn app:app --host 0.0.0.0 --port 8000
```

## API Endpoints

- `GET /api/health` - Health check endpoint
- `GET /api/metrics/cpu` - CPU metrics
- `GET /api/metrics/memory` - Memory usage statistics
- `GET /api/metrics/disk` - Disk space information

## Project Structure

```
SysPulse/
├── src/
│   ├── app.py              # FastAPI application
│   ├── frontend/           # Frontend assets
│   └── requirements.txt    # Python dependencies
├── docker/
│   ├── Dockerfile         # Application Dockerfile
│   └── docker-compose.yml # Docker Compose configuration
├── tests/
│   └── test_app.py        # Test cases
└── README.md              # Project documentation
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

## Acknowledgments

- FastAPI for the web framework
- Prometheus for metrics collection
- Grafana for visualization
- psutil for system metrics

## Support

If you encounter any issues or have questions, please:
1. Check the [Issues](https://github.com/yourusername/SysPulse/issues) page
2. Create a new issue if your problem isn't already listed

## Roadmap

- [ ] Add authentication
- [ ] Support for multiple systems
- [ ] Custom alerting rules
- [ ] Historical data analysis
- [ ] Mobile app support

## Authors

- Muhammad Shameer Awais - Initial work - [YourGitHub](https://github.com/ShameerAwais)

## Acknowledgments

- Thanks to all contributors who have helped shape this project
- Inspired by various system monitoring tools
