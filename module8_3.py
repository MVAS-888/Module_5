#Завдання 3
#Створіть список товарів в інтернет-магазині. Серіалізуйте його за допомогою pickle та збережіть у JSON.
import pickle
import json

products = [
    {"id": 1, "name": "Laptop", "price": 1200.50, "stock": 10},
    {"id": 2, "name": "Smartphone", "price": 699.99, "stock": 25},
    {"id": 3, "name": "Headphones", "price": 149.99, "stock": 50},
    {"id": 4, "name": "Smartwatch", "price": 199.99, "stock": 15},
]

with open("products.pkl", "wb") as pkl_file:
    pickle.dump(products, pkl_file)

with open("products.json", "w") as json_file:
    json.dump(products, json_file, indent=4)

print("Products saved in 'products.pkl' (Pickle) and 'products.json' (JSON')")

with open("products.pkl", "rb") as pkl_file:
    loaded_products_pickle = pickle.load(pkl_file)
    print("📦 Loaded from Pickle:", loaded_products_pickle)

with open("products.json", "r") as json_file:
    loaded_products_json = json.load(json_file)
    print("🛒 Loaded from JSON:", loaded_products_json)

