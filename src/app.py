import psutil
from fastapi import FastAPI

app = FastAPI()

# Function to convert bytes to GB
def bytes_to_gb(b):
    return round(b / (1024 ** 3), 2)

@app.get("/health")
def read_health():
    return {"status": "OK", "message": "SysPulse is live!"}

@app.get("/metrics/memory")
def get_memory_metrics():
    mem = psutil.virtual_memory()
    return {
        "total_gb": bytes_to_gb(mem.total),
        "used_gb": bytes_to_gb(mem.used),
        "free_gb": bytes_to_gb(mem.available),
        "percent": mem.percent,
    }

@app.get("/metrics/disk")
def get_disk_metrics():
    disk = psutil.disk_usage("/")
    return {
        "total_gb": bytes_to_gb(disk.total),
        "used_gb": bytes_to_gb(disk.used),
        "free_gb": bytes_to_gb(disk.free),
        "percent": disk.percent,
    }

@app.get("/metrics/cpu")
def get_cpu_metrics():
    return {"cpu_percent": psutil.cpu_percent(interval=1)}

@app.get("/health")
def health():
    return {"status": "healthy"}
