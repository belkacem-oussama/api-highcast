from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Pour avoir votre empreinte écologique, allez sur /calculate et renseignez vos informations."

def test_home_footprint_valid_json():
    response = client.post(
        "/calculate/",
        json={
            "type": "electricity",
            "electricity_unit" : "kwh",
            "electricity_value" : 1.14,
            "country" : "fr"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Voici votre empreinte carbone."
    assert "emission_carbone" in data
    assert data["unité"] == "kgCO2e"
