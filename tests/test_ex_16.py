import requests

def test_get_other_user_data_with_authentication():
    auth_data = {"username": "user1", "password": "password1"}
    auth_response = requests.post("https://playground.learnqa.ru/api/user/login", data=auth_data)
    auth_cookies = auth_response.cookies

    user_id = 2
    response = requests.get(f"https://playground.learnqa.ru/api/user/{user_id}", cookies=auth_cookies)

    assert response.status_code == 200, f"Unexpected status code {response.status_code}"

    response_data = response.json()
    assert "username" in response_data, "Username is not present in response"
    assert len(response_data) == 1, f"Unexpected response data: {response_data}"
