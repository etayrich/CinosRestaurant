class Order:
    """Class representing an order."""
    TAX_RATE = 0.0725

    def __init__(self):
        """Initialize an order."""
        self._items = []

    def get_items(self):
        """Get the items in the order."""
        return self._items

    def get_num_items(self):
        """Get the number of items in the order."""
        return len(self._items)

    def get_total(self):
        """Get the total price of the order."""
        total = 0
        for item in self._items:
            total += item.get_cost()
        return total

    def add_item(self, item):
        """Add any food or drink to the order."""
        self._items.append(item)

    def remove_item(self, index):
        """Remove any food or drink from the order based on index."""
        if 0 <= index < len(self._items):
            del self._items[index]

    def generate_receipt(self):
        """Generate a receipt for the order."""
        receipt = ""
        for item in self._items:
            receipt += f"{item.get_type()} with {', '.join(item.get_toppings())}: ${item.get_cost():.2f}\n"
        receipt += f"Total: ${self.get_total():.2f}\n"
        receipt += f"Tax: ${self.TAX_RATE * self.get_total():.2f}\n"
        receipt += f"Overall Total: ${(1 + self.TAX_RATE) * self.get_total():.2f}\n"
        return receipt