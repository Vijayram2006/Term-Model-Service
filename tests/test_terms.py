from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
import uuid

def test_create_term():
    unique_term_id = f"TEST_{uuid.uuid4()}"

    response = client.post(
        "/terms",
        json={
            "turf_rid": 1,
            "term_id": unique_term_id,
            "language": "en",
            "country": "US",
            "term_name": "Test Term"
        }
    )

    assert response.status_code == 200

    assert response.json()["term_id"] == unique_term_id

