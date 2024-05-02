import requests

BASE = "http://127.0.0.1:5000/"

if __name__ == "__main__":
    data = {
        "name": "something",
        "price": 12345
    }

    response = requests.get(BASE + "products")
    print(response.json(), response.status_code)

    response = requests.post(BASE + "products", json=data)
    print(response.json(), response.status_code)