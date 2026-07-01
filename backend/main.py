from fastapi import FastAPI

from backend.api.health import router as health_router
from backend.core.config import APP_NAME, API_VERSION, API_DESCRIPTION

app = FastAPI(
    title=APP_NAME,
    description=API_DESCRIPTION,
    version=API_VERSION,
)


@app.get("/")
def read_root():
    return {"message": "AI Crypto Copilot API is running"}


app.include_router(health_router)