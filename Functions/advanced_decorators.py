# 1 Decorators with parameters
def add_symbol(symbol):
    def decorator(func):
        def wrapper(name):
            return func(name) + symbol
        return wrapper
    return decorator

@add_symbol('!')
def greet(name):
    return f'Hello {name}'

print(greet('Alicem'))


# 2 Classes can be decorators too
class add_symbol():
    def __init__(self, symbol):
        self.symbol = symbol
    
    def __call__(self, func):
        def wrapper(name):
            return func(name) + self.symbol
        return wrapper

decorator = add_symbol('!')

@decorator
def greet(name):
    return f'Hello {name}'

print(greet('A.C.K'))


# 3 Decorators for admin stuff eg. logging/timing stuff
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s:%(levelname)s:%(asctime)s:%(message)s',
    filename='app.log'
)
logger = logging.getLogger('my_logger')

def log(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            logger.info(message)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log('God Save The Queen!')
def greet(name):
    return f'Hello {name}'

print(greet('Alicem Koyun'))


# 4 @cache, @lru_cache Decorator For Fibonacci Series
'''
@lru_cache uses algoritm = Least Recently Used and it has a parameter
max_size which allow us to set the max amount of cache element, then 
removes the least used items to make room for new ones. Python v 3.2
@cache > no max_size or sth. it caches everything.Python v 3.9
'''
from functools import cache
from time import perf_counter

def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)


@cache
def fib_cached(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib_cached(n-1) + fib_cached(n-2)

start = perf_counter()
print(fib(40))
print(f'{fib.__name__} took {perf_counter() - start} seconds')
# fib took 11.105151416999888 seconds

start = perf_counter()
print(fib_cached(40))
print(f'{fib_cached.__name__} took {perf_counter() - start} seconds')
# fib_cached took 2.287500001330045e-05 seconds


# @wraps 
from functools import wraps

def add_exclamation(func):
    @wraps(func)
    def wrapper(name):
        return func(name) + '!'
    return wrapper

@add_exclamation
def greet(name):
    """returns name

    Args:
        name (str): takes names
    """
    return f'Hello {name}'

print(greet.__name__) # greet 
print(greet.__doc__) # returns name Args: name(str): takes names