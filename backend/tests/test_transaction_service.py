from fastapi import HTTPException

from backend.services.transaction_service import (
    labels_from_storage,
    labels_to_storage,
    normalize_labels,
    suggest_transaction_labels,
)


def run_transaction_service_checks():
    assert normalize_labels([" DeFi ", "stablecoin", "defi"]) == ["defi", "stablecoin"]
    assert labels_to_storage(["defi", "stablecoin"]) == "defi,stablecoin"
    assert labels_from_storage("defi,stablecoin") == ["defi", "stablecoin"]
    assert labels_from_storage("") == []

    assert suggest_transaction_labels("swap", "USDC", 15000) == [
        "defi",
        "stablecoin",
        "large_transaction",
    ]

    assert suggest_transaction_labels("fee", "ETH", 3) == [
        "gas",
        "expense",
        "small_transaction",
    ]

    assert suggest_transaction_labels("staking_reward", "ETH", 25) == [
        "staking",
        "income",
    ]

    try:
        normalize_labels(["bad_label"])
    except HTTPException as error:
        assert error.status_code == 400
    else:
        raise AssertionError("Invalid labels should raise HTTPException")

    print("Transaction service checks passed.")


if __name__ == "__main__":
    run_transaction_service_checks()