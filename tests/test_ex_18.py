import requests
import pytest


class TestUserDelete:
    def test_delete_user_unauthorized(self):
        # Попытка удалить пользователя без авторизации
        user_id = 2
        response = requests.delete(f"https://playground.learnqa.ru/api/user/{user_id}")
        assert response.status_code == 400, f"Unexpected status code {response.status_code}"

    @pytest.mark.positive
    def test_delete_user_positive(self):
        # Создание нового пользователя
        new_user_data = {"email": "newuser@example.com", "password": "password"}
        create_response = requests.post("https://playground.learnqa.ru/api/user/", data=new_user_data)
        assert create_response.status_code == 201, f"Unexpected status code {create_response.status_code}"

        # Авторизация под созданным пользователем
        auth_data = {"email": "newuser@example.com", "password": "password"}
        auth_response = requests.post("https://playground.learnqa.ru/api/user/login", data=auth_data)
        assert auth_response.status_code == 200, f"Unexpected status code {auth_response.status_code}"
        auth_cookies = auth_response.cookies

        # Удаление пользователя
        user_id = create_response.json()["id"]
        delete_response = requests.delete(f"https://playground.learnqa.ru/api/user/{user_id}", cookies=auth_cookies)
        assert delete_response.status_code == 200, f"Unexpected status code {delete_response.status_code}"

        # Попытка получить данные удаленного пользователя
        get_response = requests.get(f"https://playground.learnqa.ru/api/user/{user_id}")
        assert get_response.status_code == 404, f"Unexpected status code {get_response.status_code}"

    def test_delete_user_as_other_user(self):
        # Создание нового пользователя
        new_user_data = {"email": "newuser@example.com", "password": "password"}
        create_response = requests.post("https://playground.learnqa.ru/api/user/", data=new_user_data)
        assert create_response.status_code == 201, f"Unexpected status code {create_response.status_code}"

        # Авторизация под созданным пользователем
        auth_data = {"email": "newuser@example.com", "password": "password"}
        auth_response = requests.post("https://playground.learnqa.ru/api/user/login", data=auth_data)
        assert auth_response.status_code == 200, f"Unexpected status code {auth_response.status_code}"
        auth_cookies = auth_response.cookies

        # Авторизация под другим пользователем
        other_user_data = {"email": "vinkotov@example.com", "password": "1234"}
        other_user_auth_response = requests.post("https://playground.learnqa.ru/api/user/login", data=other_user_data)
        assert other_user_auth_response.status_code == 200, f"Unexpected status code {other_user_auth_response.status_code}"
        other_user_auth_cookies = other_user_auth_response.cookies

        # Попытка удалить пользователя под другим пользователем
        user_id = create_response.json()["id"]
        delete_response = requests.delete(f"https://playground.learnqa.ru/api/user/{user_id}",
                                          cookies=other_user_auth_cookies)
        assert delete_response.status_code == 403, f"Unexpected status code {delete_response.status_code}"
