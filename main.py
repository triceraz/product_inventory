#Product Inventory Project - Create an application which manages an inventory of products. Create a product class which has a price, id, and quantity on hand. Then create an inventory class which keeps track of various products and can sum up the inventory value.

from inventory import Product, Inventory
from gui import *


def main():
    apple = Product("Apple",2,1,5)
    orange = Product("Orange", 3, 2, 10)
    inventory = Inventory([apple, orange])


    gui = InventoryGUI(inventory)
    gui.display_products()
    gui.run()


if __name__=="__main__":
    main()
