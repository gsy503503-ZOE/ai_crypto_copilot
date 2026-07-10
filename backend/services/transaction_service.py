from typing import Optional

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

ALLOWED_LABELS = {
    "defi",
    "cex",
    "stablecoin",
    "large_transaction",
    "small_transaction",
    "income",
    "expense",
    "gas",
    "nft",
    "bridge",
    "staking",
    "airdrop",
}


def normalize_category(category: str) -> str:
    normalized_category = category.strip().lower()

    if normalized_category not in ALLOWED_CATEGORIES:
        raise HTTPException(status_code=400, detail="Invalid transaction category")

    return normalized_category


def normalize_labels(labels: list[str]) -> list[str]:
    normalized_labels = []

    for label in labels:
        normalized_label = label.strip().lower()

        if normalized_label == "":
            continue

        if normalized_label not in ALLOWED_LABELS:
            raise HTTPException(status_code=400, detail="Invalid transaction label")

        if normalized_label not in normalized_labels:
            normalized_labels.append(normalized_label)

    return normalized_labels


def labels_to_storage(labels: list[str]) -> str:
    return ",".join(normalize_labels(labels))


def labels_from_storage(labels: Optional[str]) -> list[str]:
    if labels is None or labels == "":
        return []

    return [label for label in labels.split(",") if label]


def suggest_transaction_labels(category: str, token_symbol: Optional[str], value_usd: Optional[float]) -> list[str]:
    labels = []
    normalized_category = normalize_category(category)
    normalized_token_symbol = ""

    if token_symbol:
        normalized_token_symbol = token_symbol.strip().upper()

    if normalized_category in {"swap", "bridge"}:
        labels.append("defi")

    if normalized_category == "fee":
        labels.append("gas")
        labels.append("expense")

    if normalized_category == "airdrop":
        labels.append("airdrop")
        labels.append("income")

    if normalized_category == "staking_reward":
        labels.append("staking")
        labels.append("income")

    if normalized_category == "bridge":
        labels.append("bridge")

    if normalized_token_symbol in {"USDC", "USDT", "DAI"}:
        labels.append("stablecoin")

    if value_usd is not None:
        if value_usd >= 10000:
            labels.append("large_transaction")
        elif value_usd <= 10:
            labels.append("small_transaction")

    return normalize_labels(labels)


def transaction_to_response(transaction) -> dict:
    return {
        "id": transaction.id,
        "wallet_address": transaction.wallet_address,
        "tx_hash": transaction.tx_hash,
        "chain": transaction.chain,
        "category": transaction.category,
        "token_symbol": transaction.token_symbol,
        "amount": transaction.amount,
        "value_usd": transaction.value_usd,
        "timestamp": transaction.timestamp,
        "note": transaction.note,
        "labels": labels_from_storage(transaction.labels),
    }
