#####################       DESIGN PATTERNS      #######################
'''
Design patterns are essential tools for software developers, providing 
tested solutions to common problems in software design. In Python, 
certain patterns stand out for their frequent use and practicality. 
We’ll focus on some of the most usable patterns, explaining how they 
work and where they can be effectively applied.
'''

### SINGLETON PATTERN (Creational)
'''
Purpose: Ensures that a class has only one instance and provides a 
global point of access to it.
How It Works: The Singleton pattern restricts the instantiation of a 
class to one object. It is implemented by creating a class that checks 
whether an instance of itself already exists and creates a new one if 
it doesn’t.
Use Case: Singleton is often used in configurations, logging, database 
connections, file managers where a single point of control is necessary.
'''
class Singleton:
    _instance = None

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance


# Usage
s1 = Singleton.getInstance()
s2 = Singleton.getInstance()
assert s1 is s2  # Both are the same instance



### FACTORY METHOD PATTERN (Creational)
'''
Purpose: Provides an interface for creating objects in a superclass but
allows subclasses to alter the type of objects that will be created.
How It Works: The Factory Method pattern works by defining an interface
for creating an object but delegates the instantiation to subclasses. 
This pattern is particularly useful when the process of construction is 
complex.
Use Case: Creating different UI elements based on user preferences, 
different payment processing methods based on region.
'''
class Polygon:
    def __init__(self, sides):
        self.sides = sides


class Triangle(Polygon):
    # Implementation specific to Triangle
    pass


class Square(Polygon):
    # Implementation specific to Square
    pass

class PolygonFactory:
    @staticmethod
    def get_polygon(sides):
        if sides == 3:
            return Triangle(sides)
        if sides == 4:
            return Square(sides)
        raise ValueError("No such polygon")


# Usage
triangle = PolygonFactory.get_polygon(3)
square = PolygonFactory.get_polygon(4)



### OBSERVER PATTERN (Behavioral)
'''
Purpose: Allows an object to notify other objects (observers) about 
changes in its state.
How It Works: The Observer pattern is a publish-subscribe model where 
the subject maintains a list of observers and notifies them in case of
state changes. This pattern is crucial for implementing distributed 
event handling systems.
Use Case: Used in implementing event handling systems, data broadcasting,
or implementing real-time data feeds like stock market updates.
'''
class NewsPublisher:
    def __init__(self):
        self._subscribers = []
        self._latest_news = None

    def attach(self, subscriber):
        self._subscribers.append(subscriber)

    def detach(self, subscriber):
        self._subscribers.remove(subscriber)

    def notify_subscribers(self):
        for subscriber in self._subscribers:
            subscriber.update()

    def add_news(self, news):
        self._latest_news = news
        self.notify_subscribers()

    def get_news(self):
        return self._latest_news


class Subscriber:
    def update(self):
        # Get the latest news from the publisher
        pass


# Usage
publisher = NewsPublisher()
subscriber1 = Subscriber()
publisher.attach(subscriber1)
publisher.add_news("Breaking News: Python 4.0 Released!")



### STRATEGY PATTERN (Behavioral)
'''
Purpose: Enables selecting an algorithm’s implementation at runtime.
How It Works: The Strategy pattern involves defining a family of
algorithms, encapsulating each one, and making them interchangeable. 
The algorithm can vary independently from clients that use it.
Use Case: The Strategy pattern is useful in scenarios where you need to 
dynamically switch algorithms based on context, such as different data 
compression or encryption methods.
'''
from abc import ABC, abstractmethod


class CompressionStrategy(ABC):
    @abstractmethod
    def compress(self, files):
        pass


class ZipCompressionStrategy(CompressionStrategy):
    def compress(self, files):
        # ZIP compression logic
        return "Compressed with ZIP"


class RarCompressionStrategy(CompressionStrategy):
    def compress(self, files):
        # RAR compression logic
        return "Compressed with RAR"


class Compressor:
    def __init__(self, strategy: CompressionStrategy):
        self.strategy = strategy

    def compress_files(self, files):
        return self.strategy.compress(files)


# Usage
files = ["file1.txt", "file2.jpg"]
zip_compressor = Compressor(ZipCompressionStrategy())
rar_compressor = Compressor(RarCompressionStrategy())
print(zip_compressor.compress_files(files))  # Compressed with ZIP
print(rar_compressor.compress_files(files))  # Compressed with RAR



### ADAPTER PATTERN (Structural)
'''
Purpose: Allows incompatible interfaces to work together.
How It Works: The Adapter pattern acts as a bridge between two 
incompatible interfaces. This pattern involves a single class, 
the Adapter, which joins functionalities of independent or incompatible 
interfaces.
Use Case: Commonly used in software libraries and frameworks, where the 
functionality provided by a class needs to be made compatible with the 
rest of the system.
'''
class EuropeanSocketInterface:
    def voltage(self):
        pass


class AmericanSocketInterface:
    def voltage(self):
        pass


class EuropeanSocket(EuropeanSocketInterface):
    def voltage(self):
        return 230


class AmericanSocket(AmericanSocketInterface):
    def voltage(self):
        return 110


class SocketAdapter(EuropeanSocketInterface):
    def __init__(self, socket):
        self.socket = socket

    def voltage(self):
        return self.socket.voltage()


# Usage
american_socket = AmericanSocket()
adapter = SocketAdapter(american_socket)
print(f"Adapter voltage: {adapter.voltage()}V")  # Adapter voltage: 110V




### PROXY PATTERN (Structural)
'''
Purpose: Provides a surrogate or placeholder for another object to 
control access to it. This is useful for lazy loading, controlling access, 
or logging, among other things.
How It Works: In the Proxy pattern, a proxy object is used to interface 
with the real object. The proxy can intercept calls to the real object, 
adding additional actions like lazy initialization, access control, or logging.
Use Case: The Proxy pattern is widely used in networked applications to 
add a layer between clients and servers (e.g., to handle remote method invocation). 
It’s also useful in scenarios where object creation is resource-intensive, 
and you want to delay it until the object is actually needed.
'''
class Image:
    def display(self):
        pass


class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_from_disk()

    def load_from_disk(self):
        print(f"Loading {self.filename}")

    def display(self):
        print(f"Displaying {self.filename}")


class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()


# Usage
image = ProxyImage("test_image.jpg")
image.display()  # Loads and displays image
image.display()  # Only displays image, as it's already loaded





########################### METACLASSES ################################
'''
In Python, metaclasses are the ‘classes of classes’. They define how a 
class behaves. A metaclass is to a class what a class is to an instance. 
Metaclasses are used to create classes with specific traits or behaviors.

Imagine a framework that requires all classes to have a certain set of 
methods or attributes. A metaclass can automatically add these or enforce 
rules, ensuring consistency across the framework.
'''
class UniformMeta(type):
    def __new__(cls, name, bases, dct):
        # Ensure each class has a required_method
        assert 'required_method' in dct, "Missing required_method"
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=UniformMeta):
    def required_method(self):
        pass

#This approach is often seen in large-scale frameworks where consistent 
# behavior across different modules or plugins is crucial.
''' 
cls: UniformMeta sinifini temsil eder.
name: MyClass olarak adlandirilan sinifin adini temsil eder.
bases: MyClass'in herhangi bir sinifi miras alip almadiğini belirleyen 
bir tuple'dir. Ancak, örneğin, bu özel durumda bases boş bir tuple olacaktir, 
çünkü MyClass hiçbir sinifi miras almamaktadir.
dct: MyClass sinifinin üye değişkenleri ve metotlarini içeren bir sözlüktür. 
required_method adli bir metodu içermesi gerektiği kontrol edilmektedir.
'''

'''
DIFFERENCE BETWEEN ABC AND METACLASS
Abstract Base Class (ABC):

ABCs define classes with one or more abstract (unimplemented) methods.
They provide an interface that classes must adhere to, specifying certain behavior.
Defined using the abc module.
Classes must inherit from an ABC and implement the specified abstract methods.
ABCs serve the purpose of organizing code and enforcing a specific interface.
Metaclass:

Metaclasses are used to control the process of creating classes.
A metaclass determines how classes are created and can customize their behavior.
Typically, they customize the class creation process using the __new__ and/or __init__ methods.
Metaclasses are often used to control or modify the structure of a particular 
class hierarchy.While metaclasses and abstract base classes share some
similarities in their tasks, they fundamentally serve different purposes.
Metaclasses control the class creation process, whereas ABCs are used 
to define and enforce a specific behavior. In most cases, ABCs are preferred
for more specific use cases, while metaclasses are used for broader and
more customized scenarios.
'''




######################## DEPENDENCY INJECTION ##########################
'''
Dependency Injection (DI) is a technique that promotes loose coupling and 
easier testing by injecting dependencies into objects rather than 
hard-coding them.

In a web application, a service class responsible for accessing a database 
can be injected into a controller class, making it easier to swap out
database backends or to mock the database layer in tests.
'''
class DatabaseService:
    def get_data(self):
        return "Data from database"


class UserController:
    def __init__(self, db_service):
        self.db_service = db_service

    def handle_request(self):
        data = self.db_service.get_data()
        return data


# Usage
db_service = DatabaseService()
user_controller = UserController(db_service)

# Dependency Injection is extensively used in modern web frameworks and 
# large-scale applications for its flexibility and ease of testing.