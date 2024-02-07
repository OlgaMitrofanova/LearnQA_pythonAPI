import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import pytest

class TestUserRegister(BaseCase):


    @pytest.mark.parametrize("email", [
        "invalidemail.com",
        "invalidemail@com",
        "invalidemail"
    ])
    def test_create_user_with_invalid_email(email):
        data = {"email": email, "password": "password123"}
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        assert response.status_code == 400, f"Unexpected status code {response.status_code} for email {email}"

    @pytest.mark.parametrize("missing_param", [
        "email",
        "password"
    ])
    def test_create_user_with_missing_param(missing_param):
        data = {"email": "test@example.com", "password": "password123"}
        del data[missing_param]
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        assert response.status_code == 400, f"Unexpected status code {response.status_code} for missing param {missing_param}"

    def test_create_user_with_short_name(self):
        data = {"email": "test@example.com", "password": "password123", "username": "a"}
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        assert response.status_code == 400, f"Unexpected status code {response.status_code} for short username"

    def test_create_user_with_long_name(self):
        long_username = "a" * 251
        data = {"email": "test@example.com", "password": "password123", "username": long_username}
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        assert response.status_code == 400, f"Unexpected status code {response.status_code} for long username"
