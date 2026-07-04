from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.auth import router as auth_router
from backend.api.health import router as health_router
from backend.api.market import router as market_router
from backend.core.config import API_DESCRIPTION, API_VERSION, APP_NAME, settings

app = FastAPI(
    title=APP_NAME,
    description=API_DESCRIPTION,
    version=API_VERSION,
)

cors_origins = [origin.strip() for origin in settings.cors_origins.split(",") if origin.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {
        "message": "AI Crypto Copilot API is running",
        "version": API_VERSION,
    }


app.include_router(health_router)
app.include_router(auth_router)
app.include_router(market_router)