# tests/test_auth.py
import pytest
from flask import Flask
from src.configs.config import Config
from app import app

# CONFIGURE CLIENT
@pytest.fixture
def client():
    app.config.from_object(Config)  # use the app configs
    with app.test_client() as client:
        # Serve the client
        yield client 

# CONFIGURE DATA
@pytest.fixture
def user_data():
    return {
        "username":"testing_username",
        "password":"testing_password"
    }


def test_register_success(client, user_data):
    """User register Success"""
    
    response = client.post('/auth/register', json=user_data)
    
    # Verify 201 - success create
    response_data = response.data.decode('utf-8')
    assert "User registered successfully" in response_data


def test_register_missing_fields(client):
    """User Register empty fields"""
    data = {
        "username": "",
        "password": ""
    }

    response = client.post('/auth/register', json=data)
    # Verify bad request response
    assert response.status_code == 400
    assert b"Invalid data" in response.data



def test_login_invalid_credentials(client):
    """Test User Login with invalid credentials"""
    data = {
        "username": "invaliduser",
        "password": "wrongpassword"
    }
    response = client.post('/auth/login', json=data)
    
    assert b"Invalid username or password" in response.data


def test_login_success(client, user_data):
    """Success Login Test"""
    
    # Login whit user register
    response = client.post('/auth/login', json=user_data)

    # Verify response and success login
    assert response.status_code == 200
    assert b"access_token" in response.data  # Verify AccessToken
