#Product Inventory Project - Create an application which manages an inventory of products. Create a product class which has a price, id, and quantity on hand. Then create an inventory class which keeps track of various products and can sum up the inventory value.

class Product():
    def __init__(self, name, price, id, quantity):
        self.name = name
        self.price = price
        self.id = id
        self.quantity = quantity

    def __repr__(self):
        return (
                f"""
                \nName: {self.name}
                \nPrice: {self.price}
                \nId: {self.id}
                \nQuantity: {self.quantity}
                """
                )


apple = Product("Apple",2,1,5)
orange = Product("Orange", 3, 2, 10)


class Inventory():
    def __init__(self, list_of_products=None):
        if list_of_products is None:
            self.list_of_products = []
        self.list_of_products = list_of_products
    
    def __repr__(self):
        return "\n".join(
            f"{p.name}, ${p.price}, ID: {p.id}, Qty: {p.quantity}" for p in self.list_of_products
        )

    def add_product(self, product):
        self.list_of_products.append(product)

    def list_value(self):
        total_value = 0
        for product in self.list_of_products:
            total_value += product.price * product.quantity
        print(total_value)

    
inventory = Inventory([apple, orange])

print(inventory)