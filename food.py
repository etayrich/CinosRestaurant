class Food:
    """Information to create a food order."""
    
    _food_prices = {
        "Hotdog": 2.30,
        "Corndog": 2.00,
        "Ice Cream": 3.00,
        "Onion Rings": 1.75,
        "French Fries": 1.50,
        "Tater Tots": 1.70,
        "Nacho Chips": 1.90
    }

    _topping_prices = {
        "Cherry": 0.00,
        "Whipped Cream": 0.00,
        "Caramel Sauce": 0.50,
        "Chocolate Sauce": 0.50,
        "Nacho Cheese": 0.30,
        "Chili": 0.60,
        "Bacon Bits": 0.30,
        "Ketchup": 0.00,
        "Mustard": 0.00
    }

    def __init__(self, food_type):
        """Create new food type"""
        if food_type not in self._food_prices:
            raise ValueError("Unavailable or invalid food type")
        self._type = food_type
        self._toppings = []

    def get_type(self):
        """Get the type of the food."""
        return self._type

    def get_cost(self):
        """Get the cost of the food item."""
        cost = self._food_prices[self._type]
        for topping in self._toppings:
            cost += self._topping_prices[topping]
        return cost

    def get_toppings(self):
        """Get the toppings of the food item."""
        return self._toppings

    def add_topping(self, topping):
        """Add a topping to the food item."""
        if topping in self._toppings:
            raise ValueError("Duplicate topping")
        elif topping in self._topping_prices:
            self._toppings.append(topping)
        else:
            raise ValueError("Unavailable or invalid topping")