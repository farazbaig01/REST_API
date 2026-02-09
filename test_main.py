from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "online", "message": "Python API is running!"}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_create_item():
    item_data = {
        "name": "Test Item",
        "description": "This is a test item",
        "price": 9.99
    }
    response = client.post("/items", json=item_data)
    assert response.status_code == 200
    assert response.json()["data"]["name"] == "Test Item"

def test_create_item_invalid():
    # Sending a string instead of a float for price should fail
    item_data = {"name": "Broken Item", "price": "free"}
    response = client.post("/items", json=item_data)
    assert response.status_code == 422