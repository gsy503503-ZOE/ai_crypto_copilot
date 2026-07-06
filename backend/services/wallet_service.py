import re

def is_valid_evm_address(address: str) -> bool:
    pattern = r"^0x[a-fA-F0-9]{40}$"
    return re.match(pattern, address) is not None

def analyze_wallet(address: str):
    return {
        "address": address,
        "risk_level": "low",
        "total_transactions": 128,
        "insights": [
            {
                "title": "Active wallet",
                "description": "This wallet has recent transaction activity.",
            },
            {
                "title": "No obvious risk detected",
                "description": "No suspicious pattern is detected in the mock analysis.",
            },
        ],
    }