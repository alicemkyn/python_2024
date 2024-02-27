import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

import pytest
from source import shapes


def test_area():
    rectangle = shapes.Rectangle(length=10, width=20)
    assert rectangle.area() == 10 * 20
    
    
def test_perimeter():
    rectangle = shapes.Rectangle(length=10, width=20)
    assert rectangle.perimeter() == (10 * 2) + (20 * 2)

# To not initialize rectangle every time  in every function, like in the class based setup method we can just use @pytest.fixture


@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(length=10, width=20)

def test_area(my_rectangle):
    assert my_rectangle.area() == 10 * 20
    
def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == (10 * 2) + (20 * 2)


@pytest.fixture
def weird_rectangle():
    return shapes.Rectangle(length=5, width=6)


def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle