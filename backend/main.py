from fastapi import FastAPI
from backend.services.health import get_health

app = FastAPI(
    title="AI Real Estate Lead Intelligence",
    version="1.0.0"
)

@app.get("/")
def root():

    return {
        "message":
        "AI Real Estate Lead Intelligence"
    }

@app.get("/health")
def health():

    return get_health()