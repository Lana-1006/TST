class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_item(self, price):
        self.items.append(price)

    def get_total(self):
        return sum(self.items)
