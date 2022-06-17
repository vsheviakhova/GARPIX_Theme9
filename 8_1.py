import requests


def status(url):
    response = requests.get(url)
    return f"Код статуса: {response.raise_for_status}\nURL:{url}"
