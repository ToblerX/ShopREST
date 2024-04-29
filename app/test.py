import requests

BASE = "http://127.0.0.1:5000/"

if __name__ == "__main__":
    data = {
        "username": "test3",
        "password": "12345"
    }

    response = requests.get(BASE + "users")
    print(response.json(), response.status_code)

    response = requests.post(BASE + "login", json=data)
    print(response.json(), response.status_code)