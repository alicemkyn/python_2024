########################### MAGIC METHODS #############################
''' 
Magic methods in Python are special methods that begin and end with 
double underscores (__method__). They enable operator overloading and 
allow custom behavior for built-in Python functionality.
'''


################ Object Creation and Initialization ###################
'''__new__(cls, ...) : Called to create a new instance of a class. This
method is unique as it’s called before __init__ and is responsible for 
returning a new instance of your class. It's particularly useful in 
creating immutable types and in metaprogramming.
__init__(self, ...) : : Called after the instance has been created 
by __new__, this method initializes the object.'''

class Example:
    def __new__(cls):
        print("Creating Instance")
        return super(Example, cls).__new__(cls)
    
    def __init__(self):
        print("Initializing Instance")


# Usage
ex = Example()

# Output: Creating Instance
#         Initializing Instance



####################### Object Representation #########################
'''__repr__(self): Should return an unambiguous string representation of
the object, ideally one that could be used to recreate the object.
__str__(self): Returns a user-friendly string representation of the 
object.'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, aged {self.age}"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"


# Usage
p = Person("Alice", 30)
print(str(p))  # Output: Alice, aged 30
print(repr(p)) # Output: Person('Alice', 30)



###################### Comparison Magic Methods #######################
'''__eq__(self, other): Equality (==).
__ne__(self, other): Inequality (!=).
__lt__(self, other): Less than (<).
__le__(self, other): Less than or equal to (<=).
__gt__(self, other): Greater than (>).
__ge__(self, other): Greater than or equal to (>=).'''

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author


# Usage
book1 = Book("1984", "George Orwell")
book2 = Book("1984", "George Orwell")
print(book1 == book2)  # Output: True



################# Arithmetic and Bitwise Magic Methods ################
'''__add__(self, other): Addition (+).
__sub__(self, other): Subtraction (-).
__mul__(self, other): Multiplication (*).
__truediv__(self, other): Division (/).
__floordiv__(self, other): Floor Division (//).
__mod__(self, other): Modulus (%).
__pow__(self, other[, modulo]): Power (**).
__and__(self, other) : Bitwise AND operator (&)
__invert__(self): Bitwise inversion.
__or__(self, other) : OR operator(or)
__xor__(self, other) : Bitwise OR (XOR) operator(^)'''

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


# Usage
v1 = Vector(2, 4)
v2 = Vector(1, 3)
v3 = v1 + v2
print(v3.x, v3.y)  # Output: 3 7



###################### Numeric Type Conversion ########################
'''__int__(self) , __float__(self) , __complex__(self) , etc., for type 
conversion.
Attribute Access and Descriptor Methods
__getattr__(self, name), __setattr__(self, name, value), 
and __delattr__(self, name): Customize attribute access.
__getattribute__(self, name): Called unconditionally to implement 
attribute access.
__get__(self, instance, owner), __set__(self, instance, value), 
__delete__(self, instance): Implement descriptor protocol.'''

class ProtectedAttributes:
    def __init__(self):
        self._protected = "This is protected"

    def __getattr__(self, name):
        if name == "secret":
            raise AttributeError("Access Denied")
        return self.__dict__.get(name, f"{name} not found")

    def __setattr__(self, name, value):
        if name == "secret":
            raise AttributeError("Cannot modify secret")
        self.__dict__[name] = value

    def __delattr__(self, name):
        if name == "secret":
            raise AttributeError("Cannot delete secret")
        del self.__dict__[name]


# Usage
obj = ProtectedAttributes()
print(obj._protected)  # Access allowed
print(obj.missing)     # Outputs "missing not found"
# obj.secret            # Raises AttributeError: Access Denied
# obj.secret = "New"    # Raises AttributeError: Cannot modify secret



###################### Container Magic Methods ########################
'''__len__(self): Returns the length of the container. Part of the 
protocol for both sequences and mappings.
__getitem__(self, key): Defines behavior for accessing an item (obj[key]).
__setitem__(self, key, value): Assigns a value to an item (obj[key] = value).
__delitem__(self, key): Deletes an item (del obj[key]).
__iter__(self): Should return an iterator for the container.
__contains__(self, item): Checks if the container contains item.'''

class Library:
    def __init__(self, books):
        self.books = books

    def __len__(self):
        return len(self.books)

    def __getitem__(self, index):
        return self.books[index]


# Usage
library = Library(["Book1", "Book2", "Book3"])
print(len(library))        # Output: 3
print(library[1])          # Output: Book2



######################### Context Managers ###########################
'''__enter__(self) (__aenter__(self)): Called at the beginning of a with
block. It sets up the context and optionally returns an object that is 
bound to the variable after the as keyword in the with statement
__exit__(self, exc_type, exc_val, exc_tb) (__aexit__(self, exc_type, 
exc_val, exc_tv)): Called after the with block. It handles the teardown
of the context, like closing a file or releasing a lock. This method 
receives three arguments (exc_type, exc_val, exc_tb), which are used to 
manage exceptions raised within the with block.'''

class AsyncFileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    async def __aenter__(self):
        self.file = await aiofiles.open(self.filename, self.mode)
        return self.file

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.file.close()


# Usage with asyncio and aiofiles
import asyncio
import aiofiles


async def main():
    async with AsyncFileHandler('example.txt', 'w') as f:
        await f.write('Hello, async world!')


asyncio.run(main())



######################### Callable Objects ############################
'''__call__(self, [...]): Allows an instance of a class to be called as 
a function (def / async def).'''

import asyncio


class AsyncAdder:
    def __init__(self, value):
        self.value = value

    async def __call__(self, x):
        await asyncio.sleep(1)  # Simulate an async operation
        return self.value + x


# Usage in an async context
async def main():
    add_ten = AsyncAdder(10)
    result = await add_ten(20)  # Awaits the __call__ method
    print(result)  # Output: 30


asyncio.run(main())



###################### Unary Operations and More ######################
'''__neg__(self): Negative (-obj).
__pos__(self): Unary plus (+obj).
__abs__(self): Absolute value (abs(obj)).
Using __slots__
What are __slots__?
__slots__ is a special class attribute in Python. By defining __slots__
in a class, you explicitly declare that instances of that class will 
have a fixed set of attributes. This restricts the dynamic creation of 
new attributes and can lead to significant memory savings, especially 
for programs creating many instances of a class.

How to Use __slots__
You define __slots__ as an iterable (like a list or tuple) of strings 
that represent the names of the attributes.

Example: Using __slots__ in a Class'''

class Player:
    __slots__ = ['name', 'score']

    def __init__(self, name, score):
        self.name = name
        self.score = score


# Usage
player1 = Player("Alice", 100)
player1.name   # Accessible
player1.score  # Accessible
# player1.age = 25  # AttributeError: 'Player' object has no attribute 'age'
''' Benefits of Using __slots__
Memory Efficiency: By preventing the creation of __dict__ and __weakref__ 
for each instance, __slots__ can lead to significant memory savings, 
especially with a large number of instances.
Faster Attribute Access: Access to slot attributes is faster than 
accessing attributes stored in a __dict__.
Considerations and Limitations
Inheritance: If a class inherits from another class without __slots__, 
it will still have a __dict__ attribute.
Immutability: __slots__ only defines a fixed set of attributes. 
You cannot add new attributes to instances of the class (though the 
existing attributes can be modified if not made read-only).
No Default __weakref__: If you need weak references to your objects, 
you'll need to include '__weakref__' in __slots__.
Best Practices
Use __slots__ when you are sure about the fixed structure of your 
objects, and you have a large number of instances where memory savings 
will be significant.
Avoid using __slots__ if you need dynamic assignment of new attributes 
or if the class is meant to be subclassed by unknown users' classes.
By incorporating __slots__ into your classes, you can create more 
memory-efficient and performant Python applications, especially in 
scenarios where you're dealing with millions of object instances with a
fixed attribute structure.'''



############### Classmethod and Staticmethod Decorator ################
'''Another advanced concept in Python OOP is the use of classmethod and 
staticmethod decorators. These decorators modify methods in a class to 
change how they can be called and what data they can access.

Understanding @classmethod
The @classmethod decorator is used to create a method that is bound to 
the class and not the instance of the class. This means it can access 
the class attributes but not the instance attributes. The first 
parameter of a class method is usually named cls, which refers to the 
class itself.

Benefits:

Class methods can be called on the class itself, not just on instances.
They are commonly used for factory methods, which return an instance of 
the class.
Example: Using @classmethod as a Factory'''

class Person:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_full_name(cls, full_name):
        name = full_name.split()[0]
        return cls(name)


# Usage
john = Person.from_full_name("John Doe")
print(john.name)  # Output: John
#In this example, from_full_name is a class method that creates an 
# instance of Person using a full name.

####### Understanding @staticmethod
'''The @staticmethod decorator is used to create a method that doesn't 
access instance or class data. Static methods do not receive an implicit
first argument (neither self nor cls).

Benefits:

Static methods can be called on the class itself, similar to class methods.
Useful for utility functions that perform a task in isolation.
Example: Using @staticmethod'''

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32


# Usage
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(0)
print(fahrenheit)  # Output: 32.0
'''In this example, celsius_to_fahrenheit is a static method because it 
simply performs a calculation without needing any data from a 
TemperatureConverter instance or class.

Best Practices and Considerations:
Use @classmethod when you need access to class attributes or when you 
need to instantiate the class in the method (like factory methods).
Use @staticmethod when the method does not interact with the class or 
its instances, and it serves as a utility function.
Both decorators enhance the readability and organization of your code 
by clearly indicating the purpose of the method to other developers. 
They are a vital part of writing clean, maintainable, and 
well-structured object-oriented code in Python.'''



####################### Property Decorators ###########################
'''Property decorators play a crucial role. They allow for the management 
of class attributes by providing a way to implement getter, setter, 
and deleter methods, encapsulating the internal representation of 
attributes and offering a Pythonic way for attribute access and mutation.

Understanding Property Decorators
The @property decorator turns a method into a "getter" for a read-only 
attribute with the same name. To add corresponding "setter" and "deleter" 
functionality, you can decorate additional methods with @<attribute>.setter 
and @<attribute>.deleter.

Getter Method
A getter method is used to access the value of an attribute without 
directly exposing the attribute itself.

Example: Getter for a Temperature Class'''

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius


# Usage
temp = Temperature(100)
print(temp.celsius)  # 100
#In this example, celsius is a property, and its value is accessed via the 
# getter method.

####### Setter Method
'''A setter method is used to set the value of an attribute. It provides
a controlled way of setting attributes, allowing for validation or computation.

Example: Setter for Temperature Class'''

class Temperature:
    # ... (previous code)
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
        
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value


# Usage
temp = Temperature(0)
temp.celsius = -300  # Raises ValueError
#In this example, setting the celsius property is managed by the setter 
# method, which includes validation.

######## Deleter Method
'''A deleter method is used to delete an attribute. It’s useful when 
deleting an attribute requires more than just removing it from the 
object’s __dict__.

Example: Deleter for Temperature Class'''

class Temperature:
    # ... (previous code)
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.deleter
    def celsius(self):
        print("Deleting celsius")
        del self._celsius


# Usage
temp = Temperature(50)
del temp.celsius  # "Deleting celsius"
#In this example, the deleter for celsius provides a controlled way to 
# delete the _celsius attribute.

'''Benefits and Best Practices
Encapsulation: Property decorators help in encapsulating data and 
validation logic inside a class, adhering to the principles of 
encapsulation.
Readability and Maintenance: They enhance readability and make 
maintenance easier, as changes to the attribute handling can be made in 
one place.
Backward Compatibility: They allow you to introduce getter and setter 
methods without changing the class interface.
Property decorators are a powerful feature in Python for controlling 
attribute access and manipulation in a class, ensuring that the 
principles of encapsulation and abstraction are not violated. 
They provide a clean and Pythonic way to manage class attributes, 
making your code more robust, readable, and maintainable.'''