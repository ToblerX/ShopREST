import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "signup")
print(response.json(), response.status_code)

data = {
    "username": "test2",
    "password": "12345",
    "confirm": "12345"
}

response = requests.get(BASE + "signup")
print(response.json(), response.status_code)

response = requests.post(BASE + "signup", json=data)
print(response.json(), response.status_code)

response = requests.get(BASE + "signup")
print(response.json(), response.status_code)

response = requests.get(BASE + "users")
print(response.json(), response.status_code)

response = requests.get(BASE + "login")
print(response.json(), response.status_code)

response = requests.post(BASE + "login", json=data)
print(response.json(), response.status_code)

response = requests.get(BASE + "login")
print(response.json(), response.status_code)

response = requests.get(BASE + "users")
print(response.json(), response.status_code)

#response = requests.delete(BASE + "product/2")
#print(response.json())

#response = requests.get(BASE + "products")
#print(response.json())