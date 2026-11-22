
from app import app

# Test the home page
def test_home():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"Jenkins CI/CD Lab" in response.data

# Test the health endpoint
def test_health():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
