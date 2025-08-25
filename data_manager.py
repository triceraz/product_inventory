import json
from inventory import Product, Inventory


def save_to_file(products_dictionary):
    with open("products.json", "w") as data:
        json.dump(products_dictionary, data, indent=4)


def load_from_file():
    with open("products.json", "r") as data:
        products_ditctionary = json.load(data)

    list_of_products = []
    for product in products_ditctionary:
        list_of_products.append(Product(product["name"], product["price"], product["quantity"]))

    inventory = Inventory(list_of_products)
    return inventory


