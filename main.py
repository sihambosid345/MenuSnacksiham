import tkinter as tk
from tkinter import ttk
from models.menu_items import MENU_ITEMS
from utils.cart import ShoppingCart
from gui.menu_frame import MenuFrame
from gui.cart_frame import CartFrame

class ConcessionStandApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Concession Stand")
        self.root.geometry("800x600")
        
        self.cart = ShoppingCart()
        
        main_container = ttk.Frame(root)
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        self.menu_frame = MenuFrame(
            main_container,
            MENU_ITEMS,
            self.add_to_cart
        )
        self.menu_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.cart_frame = CartFrame(
            main_container,
            self.cart,
            self.remove_from_cart
        )
        self.cart_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
    def add_to_cart(self, item):
        self.cart.add_item(item)
        self.cart_frame.update_cart_display()
        
    def remove_from_cart(self, item_name):
        self.cart.remove_item(item_name)
        self.cart_frame.update_cart_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = ConcessionStandApp(root)
    root.mainloop()