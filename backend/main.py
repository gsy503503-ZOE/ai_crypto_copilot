from fastapi import FastAPI
from backend.api.health import router as health_router
from backend.core.config import APP_NAME, API_VERSION, API_DESCRIPTION
from backend.api.auth import router as auth_router
from backend.api.market import router as market_router
from backend.api.wallet import router as wallet_router
from backend.api.transactions import router as transactions_router

app = FastAPI(
    title=APP_NAME,
    description=API_DESCRIPTION,
    version=API_VERSION,
)


@app.get("/")
def read_root():
    return {"message": "AI Crypto Copilot API is running"}


app.include_router(health_router)
app.include_router(auth_router)
app.include_router(market_router)
app.include_router(wallet_router)
app.include_router(transactions_router)