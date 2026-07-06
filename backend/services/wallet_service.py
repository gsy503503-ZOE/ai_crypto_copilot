import re

from datetime import datetime


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

def calculate_risk_score(suspicious_transactions: int) -> int:
    if suspicious_transactions >= 10:
        return 90

    if suspicious_transactions >= 1:
        return 50

    return 5

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
    insights = build_wallet_insights(
        total_transactions,
        suspicious_transactions,
        risk_level,
        activity_level,
    )

    return {
        "address": address,
        "risk_level": risk_level,
        "risk_score": risk_score,
        "activity_level": activity_level,
        "total_transactions": total_transactions,
        "insights": insights,
        "analyzed_at": datetime.utcnow().isoformat(),
    }

def build_wallet_insights(
    total_transactions: int,
    suspicious_transactions: int,
    risk_level: str,
    activity_level: str,
):
    insights = [
        {
            "title": "Transaction activity",
            "description": f"This wallet has {total_transactions} transactions and shows {activity_level} activity.",
        }
    ]

    if risk_level == "high":
        insights.append(
            {
                "title": "High risk signal",
                "description": "This wallet has multiple suspicious transactions and should be reviewed carefully.",
            }
        )
    elif risk_level == "medium":
        insights.append(
            {
                "title": "Medium risk signal",
                "description": "This wallet has some suspicious activity and may need additional review.",
            }
        )
    else:
        insights.append(
            {
                "title": "Low risk signal",
                "description": "No obvious suspicious pattern was found in the mock analysis.",
            }
        )

    if suspicious_transactions > 0:
        insights.append(
            {
                "title": "Suspicious transactions",
                "description": f"This wallet has {suspicious_transactions} suspicious transactions.",
            }
        )

    return insights