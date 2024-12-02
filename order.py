class Order:
    _tax_rate = 0.0725
    """"information to create an order"""
    def __init__(self):
        self._items = []

    """add tax to total"""
    def get_tax(self):
        return self.get_total() * (1 + self._tax_rate)

    """get the items in your order"""
    def get_items(self):
        return self._items
    
    """get total of your items"""
    def get_total(self):
        total = 0
        for item in self._items:
            total += item.get_cost()
        return total
    
    """get the number of items total"""
    def get_num_items(self):
        return len(self._items)
    
    """create receipt"""
    def get_receipt(self):
        receipt_data = {
            "number of drinks": self.get_num_items(),
            "drinks": [],
            "subtotal": self.get_total(),
            "tax": self.get_total() * self._tax_rate,
            "Total": self.get_tax()
        }

        for i, drink in enumerate(self._items):
            drink_data = {
                "number of drinks": i + 1,
                "Base": drink.get_base(),
                "Size": drink.get_size(),
                "Flavors": drink.get_flavors(),
                "total cost": drink.get_total()
            } 
            receipt_data["drinks"].append(drink_data)
        return receipt_data
    
    """add drink to order"""
    def add_item(self, drink):
        self._items.append(drink)

    """remove drink from order"""
    def remove_item(self, index):
        if index < 0 or index >= len(self._items):
            raise IndexError("Invalid, cannot remove")
        self._items.pop(index)