# SysPulse 🚀

SysPulse is a lightweight system health monitoring API built using FastAPI and DevOps best practices. It exposes a simple endpoint to check the status of the application — great for containerized environments and cloud deployments.

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
