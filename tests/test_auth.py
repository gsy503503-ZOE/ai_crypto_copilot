import uuid


def test_register_login_and_me(client):
    email = f"trader-{uuid.uuid4().hex[:8]}@example.com"
    register_response = client.post(
        "/auth/register",
        json={"email": email, "password": "secret123"},
    )
    assert register_response.status_code == 200
    assert register_response.json()["email"] == email

    login_response = client.post(
        "/auth/login",
        json={"email": email, "password": "secret123"},
    )
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]

    me_response = client.get(
        "/auth/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert me_response.status_code == 200
    assert me_response.json()["email"] == email