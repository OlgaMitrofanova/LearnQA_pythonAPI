import requests
import time

def create_task():
    response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
    result = response.json()
    return result["token"], result["seconds"]

def check_status(token):
    response = requests.get(f"https://playground.learnqa.ru/ajax/api/longtime_job?token={token}")
    return response.json()

def wait_for_completion(seconds):
    time.sleep(seconds)

def get_result(token):
    response = requests.get(f"https://playground.learnqa.ru/ajax/api/longtime_job?token={token}")
    return response.json()

task_token, task_seconds = create_task()

status_before_completion = check_status(task_token)
print(f"Status before completion: {status_before_completion}")

wait_for_completion(task_seconds)

status_after_completion = check_status(task_token)
print(f"Status after completion: {status_after_completion}")

result = get_result(task_token)
print(f"Result: {result}")
