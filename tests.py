from drink import Drink
from order import Order
import pytest


def test_get_base():
    """Test the base of the drinks"""
    drink = Drink("water", "small")
    assert drink.get_base() == "water"


def test_get_flavors_empty():
    """Test if empty list is returned when flavors are not set"""
    drink = Drink("sbrite", "medium")
    assert drink.get_flavors() == []


def test_get_total():
    """Test if total returns the correct drink price."""
    drink = Drink("water", "medium")
    assert drink.get_total() == 1.75


def test_get_num_flavors_if_empty():
    """Test if get_num_flavors returns 0 when no flavors are set."""
    drink = Drink("water", "medium")
    assert drink.get_num_flavors() == 0

def test_get_num_flavors_if_not_empty():
    """Test if get_num_flavors returns the correct number of flavors when flavors are set."""
    drink = Drink("water", "medium")
    flavors = ["lemon", "mint", "blueberry"]
    drink.set_flavors(flavors)
    assert drink.get_num_flavors() == len(flavors)


def test_set_flavors():
    """Test if set_flavors method correctly sets the flavors."""
    drink = Drink("water", "medium")
    flavors = ["lemon", "mint", "blueberry"]
    drink.set_flavors(flavors)
    assert drink.get_flavors() == flavors


def test_add_flavor():
    """Test adding a valid flavor using the add_flavor method."""
    drink = Drink("water", "medium")
    drink.add_flavor("lemon")
    assert drink.get_flavors() == ["lemon"]

def test_duplicate_add_flavor():
    """Test adding a duplicate flavor and check if the correct exception is raised."""
    drink = Drink("water", "medium")
    drink.add_flavor("lemon")
    try:
        drink.add_flavor("lemon")
    except ValueError as ve:
        assert str(ve) == "Invalid or duplicate flavor"


def test_get_items_when_empty():
    """Test if get_items returns an empty array when no items are added to the order."""
    order = Order()
    assert order.get_items() == []

def test_get_num_items_when_empty():
    """Test if get_num_items returns 0 when no items are added to the order."""
    order = Order()
    assert order.get_num_items() == 0


def test_get_total_when_empty():
    """Test if get_total returns 0 when no items are added to the order."""
    order = Order()
    assert order.get_total() == 0


def test_add_item():
    """Test if add_item correctly adds a drink to the order."""
    order = Order()
    drink = Drink("water", "medium")
    order.add_item(drink)
    assert order.get_items() == [drink]


def test_remove_item_valid_index():
    """Test if remove_item removes the item at a valid index."""
    order = Order()
    drink1 = Drink("water", "medium")
    drink2 = Drink("sbrite", "medium")
    order.add_item(drink1)
    order.add_item(drink2)
    order.remove_item(0)
    assert order.get_items() == [drink2]

def test_size_and_cost():
    """Test that the size and cost are correctly set for a drink"""
    drink = Drink("sbrite", "medium")
    assert drink.get_size() == "medium"
    assert drink.get_total() == 1.75


def test_set_size_case_insensitive():
    """Tests case sensitivity"""
    drink = Drink("sbrite", "small")
    drink.set_size("MEGa")
    assert drink.get_size() == "mega"
    assert drink.get_total() == 2.15


def test_get_total_with_flavors_and_size():
    """Calculates the correct total for a drink with flavors and size."""
    drink = Drink("sbrite", "large")
    drink.add_flavor("lemon")
    assert drink.get_total() == 2.05 + 0.15


def test_get_size_accessor():
    """Returns the correct size of a drink."""
    drink = Drink("sbrite", "medium")
    assert drink.get_size() == "medium"

def test_set_size_accessor():
    """Correctly sets the size of a drink."""
    drink = Drink("sbrite", "medium")
    drink.set_size("large")
    assert drink.get_size() == "large"


