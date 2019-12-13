import pytest
import json
import requests

url = "http://127.0.0.1:5000"
headers = {
    'Content-Type': 'application/json'
}

@pytest.fixture
def client():
    session = requests.Session()

    yield session
    del session

def test_request_nologin(client):
    response = client.get(url+"/api/driver")
    res = response.json()
    print(res)
    assert response.status_code == 403

def test_login(client):
    response = login(client, "这是我瞎写的, 一定登录不上", "123")
    print(response)
    assert False

def test_register(client):
    pass

def login(client, phone, password):
    return client.post(url+"/api/login", data=dict({"phone": phone, "password": password}), headers=headers)

def logout(client):
    return client.post(url+"/api/logout", headers=headers)
