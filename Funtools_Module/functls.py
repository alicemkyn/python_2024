from functools import cache, lru_cache, cached_property, total_ordering,\
partial, reduce, singledispatch, wraps

'''
The functools module is for higher-order functions: function that act on
or return other functions. In general, any callable object can be treated
as a function for the purposes of this module.

- Most of the items in functools are decorators.
- Any callable object can be treated as a function for the purposes of functool.
- Caching: new methods came out with 3.9, 3.8
    * cache
    * cached_property
    * lru_cache
    
* total_ordering
* partial
* reduce
* singledispatch
* wraps
'''



#! cache 
'''
memoize, same as lru_cache(maxsize=None)
Because it never needs to evict old values, it is faster and smaller than
lru_cache() with a size limit.
'''

@cache
def factorial(n):
    return n * factorial(n - 1) if n else 1

factorial(10) # no previosly cached result, makes 11 recursive calls and caches
factorial(5) # just looks up cached value result
factorial(15) # makes five new recursive calls, the other 10 are cached




#! lru_cache (Least Recently Used)
'''
Pops the least used cached item if it reached the given maxsize.
'''
import time
import requests

@lru_cache(maxsize=24)
def get_webpage(module):
    '''
    Gets the specified Python module web page.
    '''
    webpage= f'https://docs.python.org/3/library/{module}.html'
    try:
        with requests.Session() as request:
            return request.get(webpage).text
    except requests.exceptions.HTTPError:
        return None

if __name__ == '__main__':
    modules = ['functools', 'os', 'sys', 'operator', 'os']
    for module in modules:
        start = time.perf_counter()
        page = get_webpage(module)
        end = time.perf_counter()
        if page:
            print(f'{module} module downloaded in {end - start:.20f} seconds')




#! cached_property
'''
This is convinient to cache class methods and attributes values.
'''

class MyClass:
    def __init__(self):
        self.value = None
    
    @cached_property
    def calculated_value(self):
        # Costly computation process going on here...
        print("Calculating value...")
        result = 42
        return result
    
obj = MyClass()
obj.calculated_value





#! total_ordering
'''
Given a class defining one or more rich comparison ordering methods,
this class decorator supplies the rest. This simplifies the effort 
involved in specifying all of the possible rich comparison operations:
__lt__(), __le__(), __gt__(), __ge__(), __eq__() methods.
'''

class Number:
    def __init__(self, value):
        self.value = value
    
    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

x = Number(5)
y = Number(10)

print(x < y, x.__lt__(y)) # True, (Two of them are same comparison, if not first one gives error)
print(x.__le__(y)) # NotImplemented 
print(x.__gt__(y)) # NotImplemented
print(x.__ge__(y)) # NotImplemented
print(x.__eq__(y)) # False

#! BUT if we use @total_ordering class decorator we should not implement
#! NotImplemented ones or we must define at least one ordering operation: < > <= >=

@total_ordering
class Number:
    def __init__(self, value):
        self.value = value
    
    def __lt__(self, other):
        return self.value < other.value

x = Number(5)
y = Number(10)
print(x < y) # True
print(x > y) # False
print(x <= y) # True
print(x >= y) # False
print(x == y) # False




#! Partial Functions
'''
Kind of like lambda. Used for creating new functions with defaults applied.
'''
def add(a, b):
    print(f'{a=}, {b=}')
    return a + b

p_add = partial(add, b=4)
print(p_add(7)) # 11





#! reduce
'''
It was built-in function before.
Apply function of two arguments cumulatively to the items of iterable, from
left to right, so as to reduce the iterable to a single value. For example,
reduce(lambda x,y : x + y, [1, 2, 3, 4, 5]) calculates:
((((1 + 2) + 3) + 4) + 5)
Perfect for calculating factorials.
'''
def add(a, b):
    print(f'{a=} {b=}')
    return a + b

print(reduce(add, [1, 2, 3, 4, 5]))
'''
Output:
a=1 b=2
a=3 b=3
a=6 b=4
a=10 b=5
15
'''

#! OR
import operator
print(reduce(operator.add, [1, 2, 3, 4, 5])) # 15




#! Function Overloading with singledispatch
'''
The singledispatch method in the functools module is a decorator used to
provide different behaviors for a single function based on different 
data types. This is particularly useful in scenarios where multiple 
dispatch or differentiation is needed. The singledispatch method allows
you to redirect a function to different implementations based on the type 
of the argument. @singledispatch is used with @(func_name).register(type)
It only looks at the first argument type and decides, doesn't look all of em.
'''

@singledispatch
def add(a, b):
    '''The generic function'''
    raise NotImplementedError('Unsupported Type')

@add.register(int)
def _(a, b):
    print('First argument type is', type(a))
    print(a + b)

@add.register(list)
def _(a,b):
    print('First argument type is', type(a))
    print(a + b)

@add.register(str)
def _(a, b):
    print('First argument type is', type(a))
    print(a + b)

add(1, 2) # 3
add('ali', 'cem') # 'alicem'
add([1, 2, 3], [4, 5, 6]) # [1, 2, 3, 4, 5, 6]
#add((9,8), (7, 6)) #! Raises NotImplemented Error, we didn't register tuple type.



#! wraps
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        '''
        A decorator
        '''
        print(f'Logging: {args=}')
        print(f'Logging: {kwargs=}')
        val = func(*args, **kwargs)
        print(f'Logging result of function: {val=}')
        return val
    
    return wrapper

@logging_decorator
def add(a, b):
    '''A function that adds two values'''
    return a + b

add(4, 5)
print(f'Name of function: {add.__name__}') # wrapper
print(f'Docstring of function: {add.__doc__}') # A decorator

#! Classic way of using decorators change the name and doc attrs of original
#! function and overwrites it. But if we use @wraps(), we'll prevent these confusion.

# FIXED with @wraps()
def logging_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        '''
        A decorator
        '''
        print(f'Logging: {args=}')
        print(f'Logging: {kwargs=}')
        val = func(*args, **kwargs)
        print(f'Logging result of function: {val=}')
        return val
    
    return wrapper

@logging_decorator
def add(a, b):
    '''A function that adds two values'''
    return a + b

add(4, 5)
print(f'Name of function: {add.__name__}') # wrapper
print(f'Docstring of function: {add.__doc__}') # A decorator