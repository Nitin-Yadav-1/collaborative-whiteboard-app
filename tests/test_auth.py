
from fastapi import status
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_login_invalid_email():
  res = client.post(
    "/login",
    json={"email": "not-exists@gmail.com", "password": "password"}
  )
  assert res.status_code == status.HTTP_401_UNAUTHORIZED
  assert res.json() == {"detail" : "Invalid Credentials"}


def test_login_invalid_password():
  res = client.post(
    "/login",
    json={"email": "test@gmail.com", "password": ""}
  )
  assert res.status_code == status.HTTP_401_UNAUTHORIZED
  assert res.json() == {"detail" : "Invalid Credentials"}


def test_login_valid():
  res = client.post(
    "/login",
    json={"email": "test@gmail.com", "password": "password"}
  )
  assert res.status_code == status.HTTP_200_OK
  data = res.json()
  assert len(data) == 1
  assert "token" in data