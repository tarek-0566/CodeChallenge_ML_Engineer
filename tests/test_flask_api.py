import pytest
from flask_api import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Welcome to the Sentence Transformer API!"}

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}

def test_predict_get_not_allowed(client):
    response = client.get('/predict')
    assert response.status_code == 405
    assert "This endpoint only supports POST requests" in response.get_json()["message"]

def test_predict_post_invalid_payload(client):
    response = client.post('/predict', json={})
    assert response.status_code == 400
    assert "Queries and product descriptions are required." in response.get_json()["error"]

def test_predict_post_valid_payload(client):
    payload = {
        "queries": ["This is a test query"],
        "product_descriptions": [
            "This is the first product description",
            "Another product description"
        ]
    }
    response = client.post('/predict', json=payload)
    assert response.status_code == 200
    data = response.get_json()
    
    # Validate the response structure
    assert data["queries"] == payload["queries"]
    assert len(data["results"]) == len(payload["queries"])

    for result in data["results"]:
        assert "query" in result
        assert result["query"] in payload["queries"]
        assert len(result["results"]) == len(payload["product_descriptions"])
        for product_result in result["results"]:
            assert "product_description" in product_result
            assert "score" in product_result
