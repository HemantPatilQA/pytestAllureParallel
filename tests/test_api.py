import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.mark.api
def test_get_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 400
    assert len(response.json()) > 0

@pytest.mark.api
@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_user_by_id(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["id"] == user_id
