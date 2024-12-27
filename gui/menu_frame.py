import tkinter as tk
from tkinter import ttk

class MenuFrame(ttk.Frame):
    def __init__(self, parent, menu_items, on_add_item):
        super().__init__(parent)
        self.menu_items = menu_items
        self.on_add_item = on_add_item
        self.create_widgets()
        
    def create_widgets(self):
        title = ttk.Label(self, text="Menu", font=('Helvetica', 16, 'bold'))
        title.pack(pady=10)
        
        for item in self.menu_items:
            btn = ttk.Button(
                self,
                text=f"{item.name} - {item.price:.2f}DH",
                command=lambda x=item: self.on_add_item(x)
            )
            btn.pack(pady=2, padx=10, fill=tk.X)