from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Oil Spill Detection System"}

def test_create_vessel():
    vessel_data = {
        "name": "Vessel 1",
        "mmsi": 123456789,
        # Add other required fields...
    }
    response = client.post("/vessels/", json=vessel_data)
    assert response.status_code == 200
    assert response.json()["mmsi"] == vessel_data["mmsi"]

def test_read_vessel():
    # First, create a vessel
    vessel_data = {
        "name": "Vessel 2",
        "mmsi": 987654321,
        # Add other required fields...
    }
    create_response = client.post("/vessels/", json=vessel_data)
    vessel_id = create_response.json()["id"]

    # Then, read the vessel
    response = client.get(f"/vessels/{vessel_id}")
    assert response.status_code == 200
    assert response.json()["mmsi"] == vessel_data["mmsi"]

def test_create_vessel_invalid_data():
    invalid_vessel_data = {
        # Missing required fields or invalid data...
    }
    response = client.post("/vessels/", json=invalid_vessel_data)
    assert response.status_code == 422  # Unprocessable Entity for validation errors
