class ShoppingCart:
    def __init__(self):
        self.items = {}
        
    def add_item(self, item):
        if item.name in self.items:
            self.items[item.name]['quantity'] += 1
        else:
            self.items[item.name] = {
                'price': item.price,
                'quantity': 1
            }
            
    def remove_item(self, item_name):
        if item_name in self.items:
            if self.items[item_name]['quantity'] > 1:
                self.items[item_name]['quantity'] -= 1
            else:
                del self.items[item_name]
                
    def get_total(self):
        return sum(item['price'] * item['quantity'] for item in self.items.values())
        
    def clear(self):
        self.items.clear()