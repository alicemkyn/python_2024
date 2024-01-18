'''
* Parameter = Place Holder

* Argument = Actual Value

* Higher Order Functions = It takes 1 or more function as an argument or
it returns a function as a value.e.g. map, filter, decorators...

* Functions are also First Class Objects like str, tuple, list, int etc...
We can assing them to a variable call them from variable, pass them as an 
argument to another function. And this properties makes them first class
objects.

* def keyword defines the functions, parameters are placeholders and 
during the defining process they are dysfunctional, they take nor global
neither other values as a reference point.

* () with paranthesis we call(execute) the function. It takes argument(s)
as a pre-defined variables or local variables and this makes them their 
reference points.

* With or without paranthesis we can assign functions to variables.e.g
a = func () -> a returns the value that returned from func itself.
a = func -> now a stores the function to execute it -> a()

* LEGB rule (Namespaces)= Local > Enclosing > Global > Built-in

* Functions first look at the local scope for the values if cant find there,
then look at the global scope. To change a value or to set a value inside
the function > global <var_name>. If it is nested function and if we want
to change the value in enclosing scope from local scope then 
nonlocal <var_name> and then in the next line we can process with the value
with denoting the actual variable.

* Position of paratemers should be like -> def foo(words, *args, **kwargs):
1- word, 2- *args-> tuple(,), 3- **kwargs -> dict{:}

* We can define func with *args, and **kwargs parameter but when we call 
the function it's not mandatory to write arguments. We can simply call the 
function like func() without referring the *args or **kwargs. If we
print(args, kwargs) -> (), {} will return them.

* After return statement no code line will work ! Using return we can return
any value we want e.g function, class, dict, int, str, etc...

* statement=deyimler > expression=ifadeler

* To see max recursion limit import sys; sys.getrecursionlimit() -> 1000
'''


###################### Basic Function Definiton ########################
def foo(val1:str, val2:int, val3:tuple, val4:dict) -> float:
    return float(val2)
###############


# If we want to take a function as a parameter we can add it like that:
# Callable[[prmtr_type1, prmtr_type2] returning_type]
from typing import Callable

my_list = [1,2,3,4,5,6]
def square(x:int, y=2) -> int:
    return x ** y

def process_list(func:Callable[[int,int],int], lst:list):
    return [func(item) for item in lst]

print(process_list(square, my_list))



# Ordered function parameters

def register(name, surname, city):
    print(f'name:{name} surname:{surname}, city:{city}')
    
register('Cem', 'Koyun', 'Ankara') # True
register('Ankara', 'Koyun', 'Cem') # Wrong because of positional parameters
register(city='Ankara', name='Cem',surname='Koyun') # Also True
# register(name='Cem','Koyun', 'Ankara') # False - If keyword arguments
# used then all arguments should be kwargs type. 



################ Default value parameter and overriding it.
def install(path='/path/to/install'):
    print('Installed to {} successfuly.'.format(path))

install() # Installed to /path/to/install successfuly.
#OR
install('new/path/to/install') # Installed to new/path/to/install successfuly.



################ *args
def multiply(*args):
    global result
    result = 1
    for i in args:
        result *= i
    print(result)

multiply(1,2,3,4,5,6,7,8,10) # 403200

print(*'TBMM', sep='.', end='.') # T.B.M.M.


def test(*args):
    print(args)

test(4,'ali', 4, 'cem',{'alicem':4444},['koyun']) # returns tuple object
# (4, 'ali', 4, 'cem', {'alicem': 4444}, ['koyun'])


################# **kwargs
def func(**kwargs):
    print(kwargs)

func(name='Cem', surname='Koyun', city='Ankara') # returns dict object
# {'name': 'Cem', 'surname': 'Koyun', 'city': 'Ankara'}

def register(**kwargs):
    print('-' * 30)
    for key, value in kwargs.items():
        print('{:<10}:{}'.format(key,value))
    print('-' * 30)

register(name='Alicem', surname="Koyun", city="Ankara")


# Question > Generate a random value from given interval and considering
# the quantity. No dups.
import random
from re import T

def randints(start=0, end=1, qty=1) ->set:
    number = set()
    while len(number) < qty:
        number.add(random.randrange(start, end))
    return number

print(randints(4, 44, 4)) # {19, 35, 11, 21}



################ Built_in Functions
# abs()
print(abs(-12)) # 12 distance to zero 

# round()
round(1.5) # 2
round(2.5) # 2 if it is .5 it will round it to even number
round(22/7, 0) # 3.0 round takes 2 parameters second param determines the #floating digit quantity
print(round(22/7, 3)) # 3.143

# all() takes iterable object if any 0, False, None returns False
# any() takes iterable object if any True, 1 or not empty obj. return True

# ascii() # takes str, list ... turns everything to str
lst = ['alicem', "koyun", 4444]
print(ascii(lst)) # str -> ['alicem', 'koyun', 4444]
print(type(ascii(lst))) # <class 'str'>
asc_rep = ascii(lst)
print(asc_rep[0]) # '['

# repr() # Same as ascii function, but ascii cant handle the Turkish or 
# other different word chars, instead it gives \u387 and similar to that.
# but repr() comes over this problem.
print(repr('şeker')) # "'şeker'"

# bool()
# bin()
# bytes() # creates byte datatype and we see b'' b letter at the beginning.
# byte is an immutable data type.

# bytearray() same as bytes but this datatype is mutable.

# chr() It can handle nums bigger than 255. Because it supports Unicode.
chr(10) # '\n'
chr(65) # 'A'
chr(305) # 'ı'

# callable() # Returns True or False depends on the arg if its func or var.
import sys, os
print(callable(sys.version)) # False it is an instance variable
print(callable(os.getcwd)) # True it is a class method(function)

# str 
bayt = bytes('kadın', encoding='utf-8')
st = str(bayt, encoding='ascii', errors='replace')
print(st) # kad��n
st1 = str(bayt, encoding='ascii', errors='ignore')
print(st1) # kadn

# eval(), exec(), globals(), locals(), compile()

# Expressions e.g
5
4 + 44
[i for i in range(10) if i % 2 in (0,1)]
len([1,2,3])
# Above, they are all expressions.

# Statements subsumes the expressions.
a = 5
if a :
    print(a)
# Or 

for i in range(3):
    print(i)
# Above they are all statements

# To recognize and differentiate those we can use eval and exec.
# eval() works with the given parameter it means that parameter is expression
# exec() this function takes statements as a parameter.

# filter() Takes two parameters and works if True.
l = [150, 373, 405, 62, 13, 19, 103]
print(list(filter(lambda x : x % 2 ==0, l))) # [150,62]

def odd(x):
    return x % 2 != 0

print(tuple(filter(odd,l))) # (373, 405, 13, 19, 103)

# hash()
# isinstance()
# map()
# max()
max(1,2,3) # 3
max([1,2,3,4,5]) # 5
llist =['ali', 'cem', 'koyun']
print(max(llist, key=len)) # 'koyun'

# range()
a = range(1,10,2)
print(a) # range object range(1, 10, 2)
print(list(a)) # [1, 3, 5, 7, 9]

# sorted() # always returns list
print(sorted('alicem')) # ['a', 'c', 'e', 'i', 'l', 'm']
print(sorted(('apple', 'strawberry', 'banana', 'cucumber', 'pineapple')))
#['apple', 'banana', 'cucumber', 'pineapple', 'strawberry']

# There will be problem with Turkish words so to fix it :
import locale
locale.setlocale(locale.LC_ALL, 'tr_TR')

names = ['selin', 'ahmet', 'pınar', 'çelik']
print(sorted(names, key=locale.strxfrm))
locale.setlocale(locale.LC_ALL, '') # reset locale

# slice() same as list slicing or chunking e.g list[0:3:1]
ls = [1,2,3,4,5,6]
print(ls[:4]) # [1, 2, 3, 4]
# OR
print(ls[slice(0,4)]) # [1, 2, 3, 4]

# sum() takes 2 parameters. First one is iterable, second one is addition value
l = [1,3,5]
print(sum(l,10)) #19

# vars() like dir() show the methods and attrs of objects
print(vars(str))
print(vars(list))
print(vars(dict))


####################### Lambda Functions
func = lambda a,b : a + b
print(func(2,2)) # 4
print(func.__code__.co_argcount) # 2
print(func.__code__.co_name) # <lambda>
print(func.__code__.co_varnames) # ('a', 'b')
print(func.__code__.co_firstlineno) # 242 # show the line num of definition.


##################### Recursive Functions
def rec(s):
    if len(s) < 1:
        return s
    else:
        print(list(s))
        return rec(s[1:])

s = 'alicem'
rec(s)
# If recursion reaches the limit it will reverse the process to return
# the given argument its previous state. To understand it clearly lets
# re-define our recursive function.

def rec(s):
    if len(s) < 1:
        return s
    else:
        print('Before', s)
        rec(s[1:])
        print('After', s)

rec('alicem')
'''
Before alicem
Before licem
Before icem
Before cem
Before em
Before m
After m
After em
After cem
After icem
After licem
After alicem
'''


##################### Nested Functions
'''
GLOBAL a= 111

def func(): # Enclosing Function
    NONLOCAL a
    global a
    a=123
    
    def func2():
        LOCAL a
        nonlocal a 
        a=321
        global a 
        a=444

Everytime ve call this nested function local variables will be deleted.
But nonlocal variables won't be deleted.
'''

def add(*added):
    total = 0
    for i in added:
        total += i
    def divide(x,y):
        nonlocal total
        total += x / y
        return total
    return divide

a = add(1,2,3,4)(4,2)
print(a) # 12.0

# OR 

a = add(1,2,3,4)
print(a(4,2)) # 12.0
