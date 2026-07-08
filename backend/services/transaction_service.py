from fastapi import HTTPException

ALLOWED_CATEGORIES = {
    "transfer",
    "swap",
    "fee",
    "airdrop",
    "staking_reward",
    "bridge",
    "unknown",
}


def normalize_category(category: str) -> str:
    normalized_category = category.strip().lower()

    if normalized_category not in ALLOWED_CATEGORIES:
        raise HTTPException(status_code=400, detail="Invalid transaction category")

    return normalized_category