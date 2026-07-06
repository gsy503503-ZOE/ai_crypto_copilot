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

def calculate_risk_score(total_transactions: int, suspicious_transactions: int) -> int:
    if total_transactions == 0:
        return 0

    suspicious_ratio = suspicious_transactions / total_transactions
    score = int(suspicious_ratio * 100)

    return min(score, 100)

def calculate_activity_level(total_transactions: int) -> str:
    if total_transactions >= 500:
        return "high"

    if total_transactions >= 50:
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

    total_transactions = wallet_data["total_transactions"]
    suspicious_transactions = wallet_data["suspicious_transactions"]
    risk_level = calculate_risk_level(suspicious_transactions)
    risk_score = calculate_risk_score(total_transactions, suspicious_transactions)
    activity_level = calculate_activity_level(total_transactions)
    insights = build_wallet_insights(total_transactions, suspicious_transactions)

    return {
        "address": address,
        "risk_level": risk_level,
        "risk_score": risk_score,
        "activity_level": activity_level,
        "total_transactions": total_transactions,
        "insights": insights,
    }

def build_wallet_insights(total_transactions: int, suspicious_transactions: int):
    insights = [
        {
            "title": "Transaction activity",
            "description": f"This wallet has {total_transactions} transactions.",
        }
    ]

    if suspicious_transactions > 0:
        insights.append(
            {
                "title": "Risk signal",
                "description": f"This wallet has {suspicious_transactions} suspicious transactions.",
            }
        )
    else:
        insights.append(
            {
                "title": "No obvious risk detected",
                "description": "No suspicious transactions were found in the mock analysis.",
            }
        )

    return insights