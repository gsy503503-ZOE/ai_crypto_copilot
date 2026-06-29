from fastapi import FastAPI

from backend.api.health import router as health_router

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "AI Crypto Copilot API is running"}


app.include_router(health_router)