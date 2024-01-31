import requests

def test_ex_12():
    response = requests.get("https://playground.learnqa.ru/api/homework_header")
    headers = response.headers
    print("Received headers:", headers)
    assert headers, "No headers received in the response"

