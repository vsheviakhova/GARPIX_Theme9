import requests


def url_status(url, attrs):
    response = requests.get(url, params=attrs)
    print(response.status_code)
    print(response.url)


parameters = {'from_global': True, 'sorting': 'price', 'text': 'd3*'}

url_status('https://www.yandex.ru/search', parameters)
