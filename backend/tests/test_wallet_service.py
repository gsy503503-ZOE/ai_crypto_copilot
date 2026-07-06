from backend.services.wallet_service import (
    analyze_wallet,
    calculate_activity_level,
    calculate_risk_score,
    is_valid_evm_address,
)


def run_wallet_service_checks():
    valid_address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"
    invalid_address = "0x123"

    assert is_valid_evm_address(valid_address) is True
    assert is_valid_evm_address(invalid_address) is False

    assert calculate_risk_score(0) == 5
    assert calculate_risk_score(1) == 50
    assert calculate_risk_score(10) == 90

    assert calculate_activity_level(0) == "low"
    assert calculate_activity_level(50) == "medium"
    assert calculate_activity_level(500) == "high"

    result = analyze_wallet(valid_address)

    assert result["address"] == valid_address
    assert result["risk_level"] == "low"
    assert result["risk_score"] == 5
    assert result["activity_level"] == "medium"
    assert result["total_transactions"] == 128

    print("Wallet service checks passed.")


if __name__ == "__main__":
    run_wallet_service_checks()