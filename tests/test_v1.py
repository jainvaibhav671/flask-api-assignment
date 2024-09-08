import pytest
from assignment.app import app
from assignment.v1.constants import CACHE_EXPIRATION_TIME
import time

PREFIX_URL="/api/v1"

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_fetch_data_success(client):
    response = client.get(f"{PREFIX_URL}/fetch-data?page=1&chunk_size=100")
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert all(isinstance(item, dict) for item in response.json)


def test_get_processed_data_success(client):
    response = client.get(f"{PREFIX_URL}/get-processed-data?page=1&chunk_size=100")
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert all(isinstance(item, dict) for item in response.json)


def test_cache_expiration(client):
    """Test that cache expires correctly for /fetch-data."""
    response1 = client.get(f"{PREFIX_URL}/fetch-data?page=1&chunk_size=100")
    assert response1.status_code == 200
    data1 = response1.get_json()

    response2 = client.get(f"{PREFIX_URL}/fetch-data?page=1&chunk_size=100")
    data2 = response2.get_json()
    assert data2 == data1  # Cached response

    print("Waiting for cache to expire...")
    # Wait for cache to expire
    time.sleep(
        CACHE_EXPIRATION_TIME
    )  # Adjust the sleep time based on the cache expiration time

    response3 = client.get(f"{PREFIX_URL}/fetch-data?page=1&chunk_size=100&shuffle=true")
    data3 = response3.get_json()
    assert response3.status_code == 200
    assert data3 != data1  # Fresh data after cache expiration
