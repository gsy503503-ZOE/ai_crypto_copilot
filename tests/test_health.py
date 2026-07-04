def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["version"] == "0.2.0"
    assert payload["cache"] in {"memory", "redis"}


def test_root_includes_version(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["version"] == "0.2.0"