import requests

def test_edit_user_unauthorized():
    # Попытка изменить данные пользователя без авторизации
    data = {"firstName": "John"}
    response = requests.put("https://playground.learnqa.ru/api/user/2", data=data)
    assert response.status_code == 401, f"Unexpected status code {response.status_code}"

def test_edit_user_authenticated_as_other_user():
    # Авторизуемся как пользователь с ID 1
    auth_data = {"username": "user1", "password": "password1"}
    auth_response = requests.post("https://playground.learnqa.ru/api/user/login", data=auth_data)
    auth_cookies = auth_response.cookies

    # Попытка изменить данные пользователя с ID 2 авторизованным пользователем с ID 1
    data = {"firstName": "John"}
    response = requests.put("https://playground.learnqa.ru/api/user/2", data=data, cookies=auth_cookies)
    assert response.status_code == 403, f"Unexpected status code {response.status_code}"

def test_edit_user_invalid_email():
    # Авторизуемся как пользователь с ID 2
    auth_data = {"username": "user2", "password": "password2"}
    auth_response = requests.post("https://playground.learnqa.ru/api/user/login", data=auth_data)
    auth_cookies = auth_response.cookies

    # Попытка изменить email пользователя на некорректный
    data = {"email": "invalidemail.com"}
    response = requests.put("https://playground.learnqa.ru/api/user/2", data=data, cookies=auth_cookies)
    assert response.status_code == 400, f"Unexpected status code {response.status_code}"

def test_edit_user_short_firstName():
    # Авторизуемся как пользователь с ID 2
    auth_data = {"username": "user2", "password": "password2"}
    auth_response = requests.post("https://playground.learnqa.ru/api/user/login", data=auth_data)
    auth_cookies = auth_response.cookies

    # Попытка изменить firstName пользователя на очень короткое значение в один символ
    data = {"firstName": "J"}
    response = requests.put("https://playground.learnqa.ru/api/user/2", data=data, cookies=auth_cookies)
    assert response.status_code == 400, f"Unexpected status code {response.status_code}"
