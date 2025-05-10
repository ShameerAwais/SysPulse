# SysPulse 🚀

A system monitoring tool for Windows, macOS, and Linux that provides real-time metrics about your system's resources.

## Features

- Real-time CPU usage monitoring
- Memory usage tracking
- Disk space monitoring
- Beautiful web interface
- Remote access support
- Cross-platform compatibility

## Installation

### From Source

1. Clone the repository:
```bash
git clone https://github.com/ShameerAwais/SysPulse.git
cd SysPulse
```

2. Install the package:
```bash
pip install -e .
```

### Using pip

```bash
pip install syspulse
```

## Usage

### Local Access

To start SysPulse with local access only (default):

```bash
syspulse
```

This will start the server at `http://127.0.0.1:8000`

### Remote Access

To allow remote access to the metrics dashboard:

```bash
syspulse --remote
```

This will start the server at `http://0.0.0.0:8000`, making it accessible from other devices on the network.

### Custom Port

To use a different port:

```bash
syspulse --port 8080
```

### All Options

```bash
syspulse --help
```

## Development

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install development dependencies:
```bash
pip install -e ".[dev]"
```

4. Run tests:
```bash
pytest
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Features

- Real-time system stats (CPU, RAM, Disk, etc.)
- Secure REST API endpoints
- ✅ Health check endpoint
- 🐳 Docker & Docker Compose setup
- ⚡ FastAPI for high performance
- CI/CD with GitHub Actions
- Infrastructure as Code (Terraform)
- Monitoring with Prometheus + Grafana

## 📦 Tech Stack

- Python + FastAPI
- Docker & GitHub Actions
- AWS (EC2, S3)
- Terraform, Prometheus, Grafana

> Developed as part of DevOps Course Project @ GIKI

## 🧪 Health Check

**Endpoint:**  
`GET /health`

Returns a JSON response indicating the status of the service.
