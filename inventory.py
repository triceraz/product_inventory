
class Product():
    counter = 1
    def __init__(self, name, price, quantity, id=None):
        if id == None:
            Product.counter += 1
            self.__id = Product.counter
        else:
            self.__id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def id(self):
        return self.__id

    def __repr__(self):
        return (
                f"""
                \nName: {self.name}
                \nPrice: {self.price}
                \nId: {self.id}
                \nQuantity: {self.quantity}
                """
                )
    
    def to_dict(self):
        return {"id": self.id, "name":self.name, "price":self.price, "quantity": self.quantity}


class Inventory():
    def __init__(self, list_of_products=None):
        self.list_of_products = list_of_products if list_of_products else []
    
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

    
