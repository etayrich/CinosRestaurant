class Drink:
    """information to create drink order"""

    """available drink base, flavors and size/cost"""
    available_base = {"water", "sbrite", "pokeacola", "Mr. Salt", "hill fog", "leaf wine"}
    available_flavor = {"lemon", "cherry", "strawberry", "mint", "blueberry", "lime"}
    _size_costs = {
        "small": 1.50,
        "medium": 1.75,
        "large": 2.05,
        "mega": 2.15
    }
    _flavor_price = 0.15

    def __init__(self, base, size):
        if base not in Drink.available_base:
            raise ValueError("Unavailable or invalid base")
        self._base = base
        self._flavor = set()
        self._size = size
        self._cost = 0.0

    """get the size of drink"""
    def get_size(self):
        return self._size

    """get base of drink"""
    def get_base(self):
        return self._base
    
    """get flavors of drink"""
    def get_flavors(self):
        return list(self._flavor)
    
    """number of avaiable flavors"""
    def get_num_flavors(self):
        return len(self._flavor)
    
    """add the flavor"""
    def add_flavor(self, flavor):
        if flavor not in Drink.available_flavor:
            raise ValueError("Unavailable flavor")
        if flavor in self._flavor:
            raise ValueError("flavor already used")
        self._flavor.add(flavor)

    """add multiple flavors"""
    def set_flavors(self, flavors):
        for flavor in flavors:
            self.add_flavor(flavor)

    """add drink size"""
    def set_size(self, size):
        size = size.lower()
        if size not in Drink._size_costs:
            raise ValueError("Invalid Size")
        self._size = size

    """total price of the drink"""
    def get_total(self):
        total = Drink._size_costs[self._size]
        total += len(self._flavor) * Drink._flavor_price
        return total