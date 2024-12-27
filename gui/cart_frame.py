import tkinter as tk
from tkinter import ttk

class CartFrame(ttk.Frame):
    def __init__(self, parent, cart, on_remove_item):
        super().__init__(parent)
        self.cart = cart
        self.on_remove_item = on_remove_item
        self.create_widgets()
        
    def create_widgets(self):
        title = ttk.Label(self, text="Panier", font=('Helvetica', 16, 'bold'))
        title.pack(pady=10)
        
        self.items_frame = ttk.Frame(self)
        self.items_frame.pack(fill=tk.BOTH, expand=True, padx=10)
        
        self.total_label = ttk.Label(self, text="Total: 0.00DH", font=('Helvetica', 12, 'bold'))
        self.total_label.pack(pady=10)
        
        self.clear_btn = ttk.Button(self, text="Vider le panier", command=self.clear_cart)
        self.clear_btn.pack(pady=5)
        
    def update_cart_display(self):
        for widget in self.items_frame.winfo_children():
            widget.destroy()
            
        for item_name, details in self.cart.items.items():
            frame = ttk.Frame(self.items_frame)
            frame.pack(fill=tk.X, pady=2)
            
            label = ttk.Label(
                frame,
                text=f"{item_name} x{details['quantity']} - {details['price'] * details['quantity']:.2f}DH"
            )
            label.pack(side=tk.LEFT)
            
            remove_btn = ttk.Button(
                frame,
                text="-",
                width=2,
                command=lambda x=item_name: self.on_remove_item(x)
            )
            remove_btn.pack(side=tk.RIGHT)
            
        self.total_label.config(text=f"Total: {self.cart.get_total():.2f}DH")
        
    def clear_cart(self):
        self.cart.clear()
        self.update_cart_display()