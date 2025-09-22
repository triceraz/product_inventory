import tkinter as tk

class InventoryGUI():
    def __init__(self, inventory):
        self.inventory = inventory
        self.root = tk.Tk()
        self.root.title("Inventory Manager")
        self.width = 800
        self.height = 600

        self.root.geometry(f"{self.width}x{self.height}")
        self.title_label = tk.Label(self.root, text="Inventory Manager", font=("Arial", 20))
        self.title_label.pack(pady=10)

        self.products_frame = tk.Frame(self.root)
        self.products_frame.pack(pady=20)
    
    def display_products(self):
        for product in self.inventory.list_of_products:
            label = tk.Label(
                self.products_frame,
                text=f"{product.name} - ${product.price} - Qty: {product.quantity} {product.id}",
                font=("Arial", 20)
            )
            label.pack(anchor="w", padx=20)

    
    def run(self):
        self.root.mainloop()


