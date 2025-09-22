from inventory import Product, Inventory
from gui import InventoryGUI
from data_manager import *

def main():
    inventory = load_from_file("products.json")
    save_to_file(inventory)

    gui = InventoryGUI(inventory)
    gui.display_products()
    gui.run()


if __name__=="__main__":
    main()
