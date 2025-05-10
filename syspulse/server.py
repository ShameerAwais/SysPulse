from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import psutil
import os
from pathlib import Path
import platform

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
    print("DEBUG: psutil.virtual_memory() =", mem)
    return {
        "total_gb": bytes_to_gb(mem.total),
        "used_gb": bytes_to_gb(mem.used),
        "free_gb": bytes_to_gb(mem.available),
        "percent": mem.percent,
    }

@app.get("/api/metrics/disk")
def get_disk_metrics():
    # Default to root partition
    if platform.system() == "Windows":
        partition = "C:\\"
    else:
        partition = "/"
    usage = psutil.disk_usage(partition)
    print(f"DEBUG: psutil.disk_usage({partition}) =", usage)
    return {
        "total_gb": bytes_to_gb(usage.total),
        "used_gb": bytes_to_gb(usage.used),
        "free_gb": bytes_to_gb(usage.free),
        "percent": usage.percent,
    }

@app.get("/api/metrics/cpu")
def get_cpu_metrics():
    # Call once to initialize, then again for real value
    psutil.cpu_percent(interval=0.1)
    cpu_percent = psutil.cpu_percent(interval=1, percpu=False)
    print("DEBUG: psutil.cpu_percent =", cpu_percent)
    return {"cpu_percent": cpu_percent} 