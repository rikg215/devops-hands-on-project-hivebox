from fastapi.testclient import TestClient

import app as app_module

from app import app, VERSION

client = TestClient(app)

def test_version():
    """test function for correct status code and version"""
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": VERSION}

def test_temperature(monkeypatch):
    """test function to test temperature endpoint"""
    fake_temp = 20.5
    monkeypatch.setattr(app_module, "box_temps", lambda: fake_temp)
    response = client.get("/temperature")
    assert response.status_code == 200
    assert response.json() == {"temperature": fake_temp}
