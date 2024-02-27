import os 
import sys
from unittest.mock import Mock

cur_dir = os.path.dirname(os.path.abspath(__file__))
par_dir = os.path.join(cur_dir, '..')
sys.path.insert(0, par_dir)

import pytest
from shopping_cart import ShoppingCart
from item_database import ItemDatabase


@pytest.fixture
def cart():
    return ShoppingCart(5)


def test_can_add_item_to_cart(cart):
    #cart = ShoppingCart(5)
    cart.add('apple')
    assert cart.size() == 1
    

def test_when_item_added_then_cart_contains_item(cart):
    #cart = ShoppingCart(5)
    cart.add('apple')
    assert 'apple' in cart.get_items()


# Assert that certain exception is raised
def test_when_add_more_than_max_items_should_fail(cart):
    #cart = ShoppingCart(5)
    for _ in range(5):
        cart.add('Apple')
    
    with pytest.raises(OverflowError):
        cart.add('Apple')
    
    
def test_can_get_total_price(cart):
    #cart = ShoppingCart()
    cart.add('Apple')
    cart.add('Orange')
    item_database = ItemDatabase()
    
    def mock_get_item(item):
        if item == 'Apple':
            return 1.0
        if item == 'Orange':
            return 2.0
        
    item_database.get = Mock(side_effect=mock_get_item)
    assert cart.get_total_price(item_database) == 3.0 