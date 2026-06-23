class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_item(self, price):
        self.items.append(price)

    def get_total(self):
        total = 0
        for item in self.items:
            total += item
        return total
        
