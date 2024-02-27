"""
What is Pytest
- Testing framework for Python
- Auto-discovery of tests
- Rich assertion introspection
- Support parameterized and fixture-based testing

++ Personal Suggestions ++
- Use Pycharm when testing, pytest integrates well with it.
- Python sometimes cant find the user defined modules path because of
the location of the module is not added in 'sys.path'. When running test
it is essential to ensure that Python can locate the modules you want to
import. To fix this issue take a look at FIX comment
"""
# FIX
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.join(current_dir, '..') # One level up to parent dir '..'
sys.path.insert(0, base_dir)
# print(__file__) # File builtin variable gives the absolute path of
# this file. /Users/username/path/to/your/script/example.py
# print(os.path.dirname(os.path.abspath(__file__)))
# /Users/alicemkoyun/Programming/Pytest/tests



# To test in terminal: pytest Pytest/tests/test_my_functions.py
import pytest
from source import my_functions
import time

# Simple Examples with Function Based Tests
def test_add():
    result = my_functions.add(number_one=1, number_two=4)
    assert result == 5


def test_divide():
    result = my_functions.divide(number_one=10, number_two=5)
    assert result == 2


def test_divide_by_zero():
    result = my_functions.divide(number_one=10, number_two=0)
    assert True


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(number_one=10, number_two=0)
        

def test_add_strings():
    result = my_functions.add(number_one='alicem', number_two='koyun')
    assert result == 'alicemkoyun'


# Mark & Parametrize
@pytest.mark.slow
def test_very_slow():
    time.sleep(2)
    result = my_functions.divide(number_one=10, number_two=5)
    assert result == 2

@pytest.mark.skip(reason='This feature is currently broken')
def test_add():
    assert my_functions.add(1, 2) == 3
    
@pytest.mark.xfail(reason='We know we cannot divide by zero')
def test_divide_zero_broken():
    my_functions.divide(4, 0)
