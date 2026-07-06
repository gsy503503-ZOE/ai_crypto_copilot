import re


MOCK_WALLET_DATA = {
    "0x742d35Cc6634C0532925a3b844Bc454e4438f44e": {
        "total_transactions": 128,
        "suspicious_transactions": 0,
    },
    "0x1111111111111111111111111111111111111111": {
        "total_transactions": 980,
        "suspicious_transactions": 18,
    },
}


def is_valid_evm_address(address: str) -> bool:
    pattern = r"^0x[a-fA-F0-9]{40}$"
    return re.match(pattern, address) is not None


def calculate_risk_level(suspicious_transactions: int) -> str:
    if suspicious_transactions >= 10:
        return "high"

    if suspicious_transactions >= 1:
        return "medium"

    return "low"


def analyze_wallet(address: str):
    wallet_data = MOCK_WALLET_DATA.get(
        address,
        {
            "total_transactions": 0,
            "suspicious_transactions": 0,
        },
    )

    risk_level = calculate_risk_level(wallet_data["suspicious_transactions"])

    return {
        "address": address,
        "risk_level": risk_level,
        "total_transactions": wallet_data["total_transactions"],
        "insights": [
            {
                "title": "Transaction activity",
                "description": f"This wallet has {wallet_data['total_transactions']} transactions.",
            },
            {
                "title": "Risk signal",
                "description": f"This wallet has {wallet_data['suspicious_transactions']} suspicious transactions.",
            },
        ],
    }