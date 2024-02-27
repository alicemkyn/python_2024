import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.insert(0, parent_dir)

import pytest
from source import shapes

@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(length=10, width=20)

@pytest.fixture
def weird_rectangle():
    return shapes.Rectangle(length=5, width=6)

