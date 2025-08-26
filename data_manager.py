import json
from inventory import Product, Inventory


def save_to_file(inventory):
    with open("products.json", "w") as data:
        json.dump(
            {"products": [p.to_dict() for p in inventory.list_of_products]},
            data, 
            indent=4
        )


def load_from_file(json_file):
    try:
        with open(json_file, "r") as data:
            data_inventory = json.load(data)
    except (json.JSONDecodeError, FileNotFoundError):
        return Inventory([])


    list_of_products = []
    for product in data_inventory.get("products", []):
        list_of_products.append(Product(product["name"], product["price"], product["quantity"], id=product["id"]))
    
    if list_of_products:
        Product.counter = max(p.id for p in list_of_products)



    inventory = Inventory(list_of_products)
    return inventory
