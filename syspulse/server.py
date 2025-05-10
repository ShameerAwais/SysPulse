from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import psutil
import os
from pathlib import Path

app = FastAPI(title="SysPulse", description="System Monitoring Tool")

# Get the package directory
PACKAGE_DIR = Path(__file__).parent

# Mount static files
app.mount("/static", StaticFiles(directory=PACKAGE_DIR / "static"), name="static")

# Setup templates
templates = Jinja2Templates(directory=PACKAGE_DIR / "templates")

def bytes_to_gb(b):
    return round(b / (1024 ** 3), 2)

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

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
    return {"cpu_percent": psutil.cpu_percent(interval=1, percpu=False)} 