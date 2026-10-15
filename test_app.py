
from app import app, add_numbers


def test_add_numbers():
    assert add_numbers(10, 20) == 30


def test_home_endpoint():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["result"] == 30


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"

