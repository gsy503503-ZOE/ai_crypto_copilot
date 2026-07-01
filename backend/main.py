from fastapi import FastAPI

from backend.api.health import router as health_router

app = FastAPI(
    title="AI Crypto Copilot API",
    description="Backend API for AI Crypto Copilot.",
    version="0.0.1",
)


@app.get("/")
def read_root():
    return {"message": "AI Crypto Copilot API is running"}


app.include_router(health_router)