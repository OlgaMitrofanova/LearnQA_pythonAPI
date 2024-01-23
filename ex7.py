import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

# 1. Запрос без параметра method
response = requests.get(url)
print("1. Запрос без параметра method:", response.text)

# 2. Запрос с неверным типом запроса HEAD
response = requests.head(url)
print("2. Запрос с неверным типом запроса:", response.text)

# 3. Запрос с правильным значением method
params = {'method': 'GET'}
response = requests.get(url, params=params)
print("3. Запрос с правильным значением method:", response.text)

# 4. Проверка всех сочетаний
methods = ['GET', 'POST', 'PUT', 'DELETE']

for method in methods:
    for query_type in methods:
        params = {'method': query_type}
        if query_type == 'GET':
            response = requests.get(url, params=params)
        else:
            data = {'method': query_type}
            response = requests.request(method, url, data=data)
        print(f"4. Запрос: {method}, Параметр method: {query_type}, Ответ: {response.text}")