from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
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

# Serve the dashboard at the root URL
@app.get("/")
def read_dashboard():
    return FileResponse(os.path.join(frontend_dir, "index.html"))

# Function to convert bytes to GB
def bytes_to_gb(b):
    return round(b / (1024 ** 3), 2)

@app.get("/api/health")
def read_health():
    return {"status": "OK", "message": "SysPulse is live!"}

@app.get("/api/metrics/memory")
def get_memory_metrics():
    # Get host memory info
    mem = psutil.virtual_memory()
    return {
        "total_gb": bytes_to_gb(mem.total),
        "used_gb": bytes_to_gb(mem.used),
        "free_gb": bytes_to_gb(mem.available),
        "percent": mem.percent,
    }

@app.get("/api/metrics/disk")
def get_disk_metrics():
    # Get host disk info for all mounted drives
    total_size = 0
    total_used = 0
    total_free = 0

    for partition in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            total_size += usage.total
            total_used += usage.used
            total_free += usage.free
        except (PermissionError, OSError):
            continue

    total_percent = (total_used / total_size * 100) if total_size > 0 else 0

    return {
        "total_gb": bytes_to_gb(total_size),
        "used_gb": bytes_to_gb(total_used),
        "free_gb": bytes_to_gb(total_free),
        "percent": round(total_percent, 2),
    }

@app.get("/api/metrics/cpu")
def get_cpu_metrics():
    # Get host CPU usage
    return {"cpu_percent": psutil.cpu_percent(interval=1, percpu=False)}
