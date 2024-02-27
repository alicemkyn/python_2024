import os
import sys
import math

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.insert(0, parent_dir)

import pytest
from source import shapes
# terminal: pytest -s 
# The -s flag : When this flag is used, the standart output and debugging
# information are printed to the terminal during the execution of tests.

# Class Based Test (setup_method, teardown_method)

class TestCircle:
    
    def setup_method(self, method): # method arg represents the test method.
        print(f'Setting up {method}')
        self.circle = shapes.Circle(10) # For every method that we have this circle object is going to be created.
        
    def teardown_method(self, method):
        print(f'Tearing down {method}')
        del self.circle
        
    def test_radius(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2
    
    def test_perimeter(self):
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius 
        assert result == expected