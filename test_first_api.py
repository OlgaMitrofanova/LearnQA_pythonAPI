import requests

class TestFirstApi:
    def test_homework_cookie(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        cookie = response.cookies.get_dict()
        print("Received cookie:", cookie)
        assert cookie, "No cookie received in the response"
