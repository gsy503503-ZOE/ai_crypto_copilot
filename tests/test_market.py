from backend.services import coingecko as coingecko_module


def test_get_coin_price(client, monkeypatch):
    monkeypatch.setattr(
        coingecko_module.coingecko_client,
        "get_price",
        lambda coin_id, vs_currency="usd": {
            "coin_id": coin_id,
            "vs_currency": vs_currency,
            "price": 50000.0,
            "change_24h": 1.5,
            "last_updated_at": 1710000000,
        },
    )

    response = client.get("/v1/market/price/bitcoin")
    assert response.status_code == 200
    payload = response.json()
    assert payload["coin_id"] == "bitcoin"
    assert payload["price"] == 50000.0
    assert payload["cached"] is False

    cached_response = client.get("/v1/market/price/bitcoin")
    assert cached_response.status_code == 200
    assert cached_response.json()["cached"] is True


def test_get_coin_prices(client, monkeypatch):
    monkeypatch.setattr(
        coingecko_module.coingecko_client,
        "get_prices",
        lambda coin_ids, vs_currency="usd": [
            {
                "coin_id": "bitcoin",
                "vs_currency": vs_currency,
                "price": 50000.0,
                "change_24h": 1.5,
                "last_updated_at": 1710000000,
            },
            {
                "coin_id": "ethereum",
                "vs_currency": vs_currency,
                "price": 3000.0,
                "change_24h": -0.5,
                "last_updated_at": 1710000000,
            },
        ],
    )

    response = client.get("/v1/market/prices?ids=bitcoin,ethereum")
    assert response.status_code == 200
    payload = response.json()
    assert len(payload["data"]) == 2
    assert payload["cached"] is False


def test_get_trending_coins(client, monkeypatch):
    monkeypatch.setattr(
        coingecko_module.coingecko_client,
        "get_trending",
        lambda: [
            {
                "coin_id": "bitcoin",
                "name": "Bitcoin",
                "symbol": "BTC",
                "market_cap_rank": 1,
                "price_btc": 1.0,
                "score": 0,
            }
        ],
    )

    response = client.get("/v1/market/trending")
    assert response.status_code == 200
    payload = response.json()
    assert payload["data"][0]["symbol"] == "BTC"
    assert payload["cached"] is False