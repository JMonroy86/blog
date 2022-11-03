from fastapi.testclient import TestClient
import pytest
import uuid


expected = {
    "username": "string",
    "password": "string",
    "email": "user@example.com",
    "is_active": True,
    "is_superuser": True,
    "id": 1
}


@pytest.mark.parametrize(
    "path,expected_status,expected_response",
    [
        ("/users/?email=user@example.com", 200, expected),
        ("/users/?email=user_totest@example.com", 404, {"detail": ["Email address not found"]}),
    ],
)
def test_get_path(test_client: TestClient, path, expected_status, expected_response):
    with test_client as ac:
        response = ac.get(path)
        assert response.status_code == expected_status
        assert response.json() == expected_response
    
    
def test_user_signup_endpoint(test_client: TestClient):
    with test_client as ac:
        user_random_email = str(uuid.uuid4())
        body = {
            "username": user_random_email,
            "password": "string",
            "email": f"{user_random_email}@example.com",
        }
        response = ac.post("/users/", json=body)
        res = response.json()
        assert response.status_code == 200
        assert "id" in res
        assert "is_active" in res
        assert "is_superuser" in res
        assert "username" in res
        assert "email" in res
        assert body["username"] == res["username"]
        assert body["password"] == res["password"]
        assert body["email"] == res["email"]


def test_user_signup_endpoint_existing_email(test_client: TestClient):
    with test_client as ac:
        user_random_email = str(uuid.uuid4())
        body = {
            "username": user_random_email,
            "password": "string",
            "email": "user@example.com",
        }
        response = ac.post("/users/", json=body)
        res = response.json()
        assert response.status_code == 404
        assert res == {"detail": ["email already exist, please, choose another one"]}


def test_user_signup_endpoint_existing_username(test_client: TestClient):
    with test_client as ac:
        user_random_email = str(uuid.uuid4())
        body = {
            "username": "string",
            "password": "string",
            "email": f"{user_random_email}@example.com",
        }
        response = ac.post("/users/", json=body)
        res = response.json()
        assert response.status_code == 404
        assert res == {"detail": ["username already exist, please, choose another one"]}


def test_user_signup_endpoint_empty_email(test_client: TestClient):
    with test_client as ac:
        body = {
            "username": "string",
            "password": "string",
            "email": "",
        }
        response = ac.post("/users/", json=body)
        res = response.json()
        assert response.status_code == 404
        assert res == {"detail": ["email doesn't have to be empty"]}
        

def test_user_signup_endpoint_empty_username(test_client: TestClient):
    with test_client as ac:
        user_random_email = str(uuid.uuid4())
        body = {
            "username": "",
            "password": "string",
            "email": f"{user_random_email}@example.com",
        }
        response = ac.post("/users/", json=body)
        res = response.json()
        assert response.status_code == 404
        assert res == {"detail": ["username doesn't have to be empty"]}
        

def test_user_signup_endpoint_empty_password(test_client: TestClient):
    with test_client as ac:
        user_random_email = str(uuid.uuid4())
        body = {
            "username": "string",
            "password": "",
            "email": f"{user_random_email}@example.com",
        }
        response = ac.post("/users/", json=body)
        res = response.json()
        assert response.status_code == 404
        assert res == {"detail": ["password doesn't have to be empty"]}