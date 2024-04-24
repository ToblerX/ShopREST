import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "products")
print(response.json())

response = requests.post(BASE + "products", json={"name" : "botinok"})
print(response.json())

response = requests.get(BASE + "products")
print(response.json())

response = requests.delete(BASE + "product/2")
print(response.json())

response = requests.get(BASE + "products")
print(response.json())