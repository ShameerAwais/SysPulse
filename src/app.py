from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from prometheus_fastapi_instrumentator import Instrumentator
import psutil
import os

app = FastAPI()

# Initialize Prometheus Instrumentator
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

# Serve static files for the frontend (HTML, CSS, JS)
frontend_dir = os.path.join(os.path.dirname(__file__), "frontend")
if os.path.exists(frontend_dir):
    app.mount("/static", StaticFiles(directory=frontend_dir), name="static")

# Function to convert bytes to GB
def bytes_to_gb(b):
    return round(b / (1024 ** 3), 2)

@app.get("/api/health")
def read_health():
    return {"status": "OK", "message": "SysPulse is live!"}

@app.get("/api/metrics/memory")
def get_memory_metrics():
    mem = psutil.virtual_memory()
    return {
        "total_gb": bytes_to_gb(mem.total),
        "used_gb": bytes_to_gb(mem.used),
        "free_gb": bytes_to_gb(mem.available),
        "percent": mem.percent,
    }

@app.get("/api/metrics/disk")
def get_disk_metrics():
    disk = psutil.disk_usage("/")
    return {
        "total_gb": bytes_to_gb(disk.total),
        "used_gb": bytes_to_gb(disk.used),
        "free_gb": bytes_to_gb(disk.free),
        "percent": disk.percent,
    }

@app.get("/api/metrics/cpu")
def get_cpu_metrics():
    return {"cpu_percent": psutil.cpu_percent(interval=1)}
