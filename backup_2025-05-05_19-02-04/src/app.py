from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def read_health():
    return {"status": "OK", "message": "SysPulse is live!"} 

