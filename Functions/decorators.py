'''
A decorator used in a function, adds some functionality and returns it. 
That means it is a feature of Python which adds functionality to the 
existing code. Modifying another part of the program within the compile
time is known as metaprogramming.

Because of this feature (extending its behavior without explicitly 
modifying it), its applications are in the real-world like debugging, 
logging, measuring execution time, authentication, etc.

General syntax for decorators are like this:
func = decorator(func)

* It is better to use @wraps() from functools to preserve __name__ and 
__doc__ attribute of a function that changed by decorator. 

*So, the decorator are first class objects in Python which extend the behavior 
of code without changing its function, with the help of decorator, i.e,. 
@decorator. We can use a decorator in function or method of a class or i
n the whole class, and also classes can also be used as decorator. 
Decorator has various applications like logging, authentication, and 
measuring execution time.
'''

def decorator(func):
    def wrapper(*args, **kwargs):
        print('Before function call')
        func(*args, **kwargs)
        print("After function call")
    return wrapper

def status():
    print("I am the famous function call!!!")

decorated = decorator(status)
decorated() # calls the wrapper -> decorated() == wrapper()
# Before function call
# I am the famous function call!!!
# After function call

status = decorator(status)
status() # Same result but this is the real decorator because we referred
# to the function name that we want to decorate and assigned it to its 
# name again. In short, we decorated the function.(Added new functionalities.)


'''
The above code is not a standard way to represent decorators because we 
have to write the same function many times, so there is another way to 
use decorators in Python. The syntax is given as below :
'''
def decorator(func):
    def wrapper(*args, **kwargs):
        print('Before the function call')
        func(*args, **kwargs)
        print("After the function call")
    return wrapper

@decorator # This does the same at line 30
def status():
    print("Function call @!")

status()
# Before the function call
# Function call @!
# After the function call




################## PRESERVING NAME AND DOCSTRING #######################
'''
To help with debugging and documentation, there are names and docstring 
in Python. These can be changed because of wrapper function in decorators.
'''

@decorator
def status():
    """
    This function returns its status
    
    """
    print("Current function status is True")

print(status.__name__) # wrapper
help(status) # wrapper(*args, **kwargs)

# To fix this we should use @wraps on the wrapper function, @wraps can
# be imported from functools module.
from functools import wraps

def decorator(func):
    @wraps(func) # This preserves the __name__ and __doc__ of func.
    # We decorated the wrapper with preserving and passing the actual func
    # thanks to wraps by giving it the func as an argument.
    def wrapper(*args, **kwargs):
        print("@wraps Before the call.")
        func(*args, **kwargs)
        print("@wraps After the call.")
    return wrapper


@decorator
def status():
    """
    This function returns its status
    
    """
    print("Current function status is True")

print(status.__name__) # status
help(status) # This function returns its status




######################### REUSING DECORATORS ###########################

def thrice(func):
    @wraps(func)
    def wrapper():
        func()
        func()
        func()
    return wrapper
        
@thrice
def print_first_name():
    print('Alicem')

@thrice
def print_second_name():
    print('Koyun')

print_first_name() # Alicem Alicem Alicem
print_second_name() # Koyun Koyun Koyun




################ DECORATORS FUNCTIONS WITH PARAMETERS ##################
def thrice(func):
    @wraps(func)
    def wrapper():
        func()
        func()
        func()
    return wrapper
        
@thrice
def print_first_name(name):
    print('name')

#print_first_name('Alicem')
#TypeError: wrapper() takes 0 positional arguments but 1 was given

#Fixed below:
def thrice(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper
        
@thrice
def print_first_name(name):
    print(name)
    
print_first_name('Alicem') # Alicem Alicem Alicem





############## RETURNING VALUES FROM DECORATED FUNCTION ################
'''
To understand this, let’s consider a function that multiplies two numbers
and returns the result of multiplication. We will also use decorator from
with above thrice decorator -
'''

def thrice(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

@thrice
def multiply(num1,num2):
    print(f"Multiplying {num1} and {num2}")
    return num1 * num2

print('The multiplication is: {}'.format(multiply(4, 5)))
'''
Output:
Multiplying 4 and 5
Multiplying 4 and 5
Multiplying 4 and 5
The multiplication is: None

The resultant value of multiplication is none; it’s because the wrapper 
function does not return anything. So we need to add return in the wrapper 
function to get the desired value.
'''


def thrice(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper

@thrice
def multiply(num1,num2):
    print(f"Multiplying {num1} and {num2}")
    return num1 * num2

print(f'The multiplication is: {multiply(4, 5)}')
'''
Output:
Multiplying 4 and 2
Multiplying 4 and 2
Multiplying 4 and 2
The multiplication is: 20

Now we have the desired value of multiplication. Also, we have returned 
to the last fun only. Hence we make sure that the last fun has returned 
otherwise it will be lost.
'''




##################### DECORATORS WITH ARGUMENTS ########################
'''
So decorators also have arguments. You should define a decorator inside 
another function that has arguments that arguments can be used inside the
decorator and return it.

Let us generalize the thrice to times, meaning we were repeating 3 times
only but now we will repeat at a given value.
'''
def times(num):
    def decorator_times(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                value = func(*args)
            print(args, kwargs)
            return value
        return wrapper
    return decorator_times

@times(num=5)
def mess(name):
    print(f"Hello, {name}")
    return len(name)

print(mess('Alicem'))
'''
Output:
Hello, Alicem
Hello, Alicem
Hello, Alicem
Hello, Alicem
Hello, Alicem
('Alicem',) {}
6
'''



#################### CHAINING OR NESTED DECORATORS #####################
def split_string(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).split()
    return wrapper

def to_upper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@split_string
@to_upper
def mess(name):
    return f'Hello, {name}'

print(mess('Alicem')) # ['HELLO,', 'ALICEM']
#order of decorators matters. first @to_upper works then @split_string
#because we cant upper the value (list) that comes from split().
#here it works like that according the flow:@split_string takes the func
#after itself, @to_upper takes the function mess() and runs the function
#takes the string from the mess, uppers it and passes it to split.




########################## FANCY DECORATORS ############################
'''
@classmethod, 
@staticmethod, 
@property, 
@func_name.setter, 
@func_name.deleter
'''


#################### DECORATING A COMPLETE CLASS #######################
'''
It is very similar to writing a function decorator. Decorator receives a 
class but not a function as argument which is the only difference between 
decorating function and decorating class. When you decorate a class, then 
class does not decorate its methods. See its structure which is similar as 
decorating function as previous -

className = decorator(className)

It means add functionality to instantiation process of class.

Consider the example, decorating a Class -
'''

from dataclasses import dataclass

@dataclass
class User:
    first_name : str
    last_name : str
    married : bool
    
user = User('Alicem', 'Koyun', True)
print(user.first_name) # Alicem
print(user.last_name) # Koyun
print(user.married) # True




####################### CLASSES AS DECORATORS ##########################
'''
You can use decorators with classes and also you can also use classes as
decorator. To store the state of the data, classes can be used. In the 
given example, we will implement a stateful decorator with a class which
records states of data, here number of classes made for a function.

You need _init_ and _call_ to make a class as a decorator. These take
function as argument and class will be used as decorator and it 
implements _call_ method. Decorator must be a callable object. Instead of 
functools.wraps, we will use functools.update_wrapper when class as a decorator.
'''
import functools

class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self,func)
        self.func = func
        self.num_calls = 0
    
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Count {self.num_calls} of {self.func.__name__!r}")
        # !r adds ' ' 
        return self.func(*args, **kwargs)

@CountCalls
def mess():
    print('Alicem')
    
mess() #Count 1 of 'mess' Alicem
mess() #Count 2 of 'mess' Alicem



################# REAL WORLD USAGE OF DECORATORS #######################
from time import time, sleep

def calc(func):
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(func.__name__, 'took', time()-t)
    return wrapper

@calc
def night(sleep_time):
    sleep(sleep_time)

night(0.4) #night took 0.40506505966186523
night(0.7) #night took 0.7050261497497559