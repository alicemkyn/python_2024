######################## OOP ##########################

class Item: # We can define it without paranthesis.
    def calculate_total_price(x, y): 
        return x * y


item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

print(Item.calculate_total_price(item1.price, item1.quantity)) # If we 
# use it like that we dont need the 'self' parameter. Because we didnt 
# call it through an instance. We called the method from the class.  

class Item(): # Or we can define it with paranthesis.
    def calculate_total_price(self,x ,y): # Self is the instance itself.
        return x * y          # Self is a convention between developers
                            # Instead of 'self' you can write anything.

item1 = Item()
item1.name = "Phone" 
item1.price = 100
item1.quantity = 5

print(item1.calculate_total_price(item1.price, item1.quantity)) #Here we
# defined 'self' parameter because we called the method through the 
# instance, otherwise it would give an error that missing parameter for 
# 'self'.




# Everytime we instantiate an object from the class we should hardcode 
# the same attributes of an object over an over againg according to how 
# many object we want to instantiate. To avoid this we will use __init__
# magic method below. 
class Item:
    def __init__(self, name, price, quantity): # As soon as an object 
# instantiated from this class this method will work no matter what. It 
# is being called immidiately while creating instance. A.k.a(constructor)
        self.name = name
        self.price = price          # Attributes that common to all objs
        self.quantity = quantity
    
    def calculate_total_price(self): # Method
        return self.price * self.quantity # We have access to this attr-
# ibutes once the instances has been created throughout the methods.So,
# we dont need to receive them as a parameters.


# item1 = Item() -> Using like that will give an missing positional 
# arguments error such as name, price, quantity

item1 = Item('Phone', 100, 5) # __init__ magic method now assigned all 
# these positional arguments as an attributes to the instance item1. 

print(item1.calculate_total_price())




# To not get the wrong datatypes as a parameter, lets specify the para-
# meter types
class Item:
    def __init__(self, name: str, price: float, quantity: int=0): # Fixed
        # Run validations for the received args
        assert price >= 0, f'Price cant be {price}'
        assert quantity >= 0, f'Quantity cant be {quantity}'
        assert isinstance(name, str), f'{name} must be str'
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def calculate_total_price(self):
        return self.price * self.quantity
    
item1 = Item('Phone', 100, 5)
item2 = Item('Laptop', 1000, 3)

print(item1.calculate_total_price())
print(item2.calculate_total_price())



#Accessing Class Attribute from instance level
class Item:
    pay_rate = 0.8 # Class attribute
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def calculate_total_price(self):
        return self.price * self.quantity
    
print(Item.pay_rate) # Accessing class attribute from class itself

item1 = Item('Phone', 100, 5)
item2 = Item('Laptop', 1000, 3)

print(item1.pay_rate) # Accessing class attribute from instance level
print(item2.pay_rate) # Accessing class attribute from instance level
# If the instance can't find the attribute in instance level __init__
# it is going to look at class level to bring it. 

# There is an magic attribute to see all the attributes in dict in class
# or in instance level. i.e :
print(Item.__dict__) # All the attributes for Class level with pay_rate
print(item1.__dict__) # All the attributes for instance level no pay_rate




class Item:
    pay_rate = 0.8
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        # self.price = self.price * pay_rate -> Won't work! Because we can
        # only access it either instance level or class level as mentioned
        # above. i.e :
        self.price *= self.pay_rate # Here we access pay_rate via instanc.
        #OR
        #self.price = self.price * Item.pay_rate # Here we access pay_rate
        #via class level. 

    def apply_discount2(self):
        self.price *= Item.pay_rate
        

item1 = Item('Phone', 100, 5) 
item1.apply_discount() # Here we dont set a new pay_rate for this
# particular instance as an attribute that's why it is going to get the 
# value from class level.
print(item1.price)

#If we want to set different discount amount for different object
item2 = Item('Laptop', 1000, 3)
item2.pay_rate = 0.7 # New pay_rate for other instance
item2.apply_discount() # Now there is a self.pay_rate above already set
# so it is not going to look to class level. 
print(item2.price)

# But if we call the apply_discount2() it wont apply the 0.7(instance 
# attribute) ratio because it was defined using class attribute ratio
# which is 0.8 (Item.pay_rate)
item2.apply_discount2()
print(item2.price)




# If we have multiple various items(instances) and if we want to see them
# all
class Item:
    
    pay_rate = 0.8 # 20% Discount
    all = [] # To see all the instances list
    
    def __init__(self, name: str, price: float, quantity: int=0):
        assert isinstance(name, str), f'{name} should be a str'
        assert price >= 0, f'{price} cant\' be negative'
        assert quantity >= 0, f'{quantity} can\'t be negative'
        
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self) # As soon as the instance is created it will add
        # it to the list (in this case it is class attribute)
                
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price *= self.pay_rate

item1 = Item('Phone', 100, 1)
print(item1.all)
item2 = Item('Laptop', 1000, 3)
item3 = Item('Cable', 10, 5)
item4 = Item('Mouse', 50,5)
item5 = Item('Keyboard', 75,5)

print(item1.all)
print(item5.all)
print(Item.all)
    
for i in Item.all:
    print(i.name) # To see the each instance name
    



#To see the objects attributes instead of seeing the type and memory 
# location when printing we'll use other magic method __repr__. 
# Class will be created same as above but __repr__ will be defined.
class Item:
    
    pay_rate = 0.8 # 20% Discount
    all = [] # To see all the instances list
    
    def __init__(self, name: str, price: float, quantity: int=0):
        assert isinstance(name, str), f'{name} should be a str'
        assert price >= 0, f'{price} cant\' be negative'
        assert quantity >= 0, f'{quantity} can\'t be negative'
        
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self) # As soon as the instance is created it will add
        # it to the list (in this case it is class attribute)
                
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price *= self.pay_rate
        
    def __repr__(self):
        return f'Item({self.name}, {self.price}, {self.quantity})'

item1 = Item('Phone', 100, 1)
item2 = Item('Laptop', 1000, 3)
item3 = Item('Cable', 10, 5)
item4 = Item('Mouse', 50,5)
item5 = Item('Keyboard', 75,5)

print(Item.all) # Now it will print the items as stated under __repr__



########################### Classmethod #############################
'''
If we'd like to instantiate lot of objects by getting data from csv file
we will use the classmethod decorator @classmethod. We will use it in
class level because we will create instances by using it so, we dont
need to use it in instance level. It is related with the class itself.
That's why we use @classmethod and tell that it is about the class and use
cls parameter not self.Here cls represents the class name itself.
Other advantage is if this class was inherited by other class we wouldn't
change the name of class Item everytime because cls references the actual
class name.
And also we can use that method to create methods that will affect and 
change or manipulate only class attributes or methods.
It should have nothing to do with instances attrs or methods.
It should be related only with class itself.
'''
import csv
from re import A

class Item:
    
    pay_rate = 0.8 
    all = [] 
    
    def __init__(self, name: str, price: float, quantity: int=0):
        assert isinstance(name, str), f'{name} should be a str'
        assert price >= 0, f'{price} cant\' be negative'
        assert quantity >= 0, f'{quantity} can\'t be negative'
        
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self) 
        
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price *= self.pay_rate
        
    def __repr__(self):
        return f'Item({self.name}, {self.price}, {self.quantity})'
    
    ########### Class method new line used here ############
    @classmethod
    def instantiate_from_csv(cls): #Parameter changes to cls because it
                                # it refers to class name itself.Because
                                # we will call it from class level.
                                # we could have write self instead of cls
                                # with no problem.
                                # But to not get confused and assume that
                                # we will call it only from class level-
                                # we give a parameter cls.
        with open('items.csv', 'r') as f: # We didnt write a specific 
            #/path/ for items.csv because they are in the same location
            #with main.py file.
            reader = csv.DictReader(f)
            items = list(reader)
            
        for item in items:
            #print(item) to see the dict of objects from csv. Pay atten-
            #tion to all values ! They are all string, even the integers.
            cls(
                name=item.get('name'),
                price=float(item.get('price')), #str to float
                quantity=int(item.get('quantity')) #str to int
            ) # to instantiate items from csv file one by one 

Item.instantiate_from_csv() # calling the method from class because it is 
# a classmethod and nothing to do with instance.
# We can call it also from the instance level i.e item1.instantiate_from
#_csv() it will work with no problem but you will never see it calling from
# instance. By convention it is always called from class level.
print(Item.all) # To check whether all the objects are created from csv file



########################### Staticmethod #############################
"""
@staticmethod doesn't take any parameter such as self and cls.
Because it has nothing to do with class attr or methods same for instances.
It doesn't change or manipulate or create any data in class or for instances.
But it is still related with class itself. That's why it defines with 
@staticmethod decorator inside a class and show that it is STATIC, no
bounds with instances attrs, methods or class attrs, methods.
We can call it from instance level but same as classmethod it is not convention
to do that. So we should call it from class level. 
Only MAIN DIFFERENCE from classmethod is it is not mandatory to give parameter
to a staticmethod such as self or cls as a first parameter.
"""
# To understand it lets create our class and define a @staticmethod
class Item:
    pay_rate = 0.8
    all = []
    
    def __init__(self, name: str, price: float, quantity: int=0):
        assert isinstance(name, str), f'{name} should be str'
        assert price >= 0, f'{price} can\'t be less then zero'
        assert quantity >= 0, f'{quantity} can\'t be less then zero'
        
        self.name = name 
        self.price = price
        self.quantity = quantity
        
        #Actions to execute
        Item.all.append(self)
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price *= self.pay_rate
        
    def __repr__(self):
        return f'Item({self.name}, {self.price}, {self.quantity})'
        
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            cls(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )
            
################ Static Method new line used here ##################
    @staticmethod
    def is_it_integer(number): # as we can see no cls or self. We will give
                            # a number from class level to check whether
                            # it's integer.
        if isinstance(number, float):
            return number.is_integer()
        elif isinstance(number, int):
            return True
        else:
            return False
    # As we can see it has nothing to do with class attrs, methods or 
    # same for instances. It is not creating or manipulating data in or
    # out of class. Only checks the value is integer or not
    
print(Item.is_it_integer(5.0)) # To check, we called it from class level.
# It is static. And only returned True




########################### INHERITANCE ################################
'''
If we have phone item i.e. we can instantiate it from our Item class.
But what if some of this phones are broken ? 
phone1 = Item()
phone1.broken = 1
The above code is correct but if we have hunderds of thousands phone ?
And how can we create methods for broken phones ?
That is when the inheritance comes handy.
We have to have separate class which has the same attributes so we can
add extra attributes and methods to manipulate them.
And it should really make sense to inherite from a parent class
and create child class in terms of functionality.
''' 

class Phone(Item): # For inheritance we pass the class as an argument
# has been already created before. So in this position the Phone class
# inherits from the Item class. Phone class is child class or sub-class,
# the Item class is parent class.
    pass

phone1 = Phone('ackPhonev10', 500, 5)
print(phone1.name) # As we can check here, it has got all the attributes
# and methods from parent class
print(Phone.all)


class Phone(Item):
    all = []
# If we want to add extra attributes as we mentioned before such as 
# broken phone attribute we need to call constructor method like that.
# NOT to copy the all the __init__ and paste then add a broken attr !!
    def __init__(
        self, name: str, 
        price: float, 
        quantity : int=0, 
        broken_phones: int =0
        ):
        # Call to super function to have access to all attrs / methods
        super().__init__(name,price,quantity )
        
        # Run validation for broken_phones
        assert broken_phones >= 0, f'broken phones {broken_phones}, cant be!'
        
        # Assign to self object
        self.broken_phones= broken_phones
        
        # Action to execute
        Phone.all.append(self)
        
phone1 = Phone('ackPhonev10', 500, 5, 1)
print(phone1.name)
print(phone1.calculate_total_price())
print(Phone.all) # This will return [(Item('ackPhonev10', 500, 5. 1))]
# In order to fix this we should head to __repr__ magic method which is
# defined in Item class and fix it as below.

class Item:
    all = []
    pay_rate = 0.8 # 20 % discount

    def __init__(self, name: str, price: float, quantity: int=0):
        assert isinstance(name, str), f'{name} is not str !'
        assert price >= 0, f'{price} is less than 0!'
        assert quantity >= 0, f'{quantity} is less than 0!'
        
        self.name = name
        self.price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self): 
        self.price *= self.pay_rate # if it can find the pay_rate at 
        # instance level it will look up to class level. It will work
        # like a charm, no worries.
        
    def __repr__(self):# Fixed here Item to self.__class__.__name__
        return  f'{self.__class__.__name__}("{self.name}",{self.price},\
{self.quantity})'
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            cls(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )
    
    @staticmethod
    def is_it_integer(number): 
        if isinstance(number, float):
            return number.is_integer()
        elif isinstance(number, int):
            return True
        else:
            return False

class Phone(Item): # And lets instantitate again
    # all = []
    
    def __init__(
        self, name: str, 
        price: float, 
        quantity : int=0, 
        broken_phones: int=0
        ):
        # Call to super function to have access to all attrs / methods
        super().__init__(name,price,quantity )
        
        # Run validation for broken_phones
        assert broken_phones >= 0, f'broken phones {broken_phones}, cant be!'
        
        # Assign to self object
        self.broken_phones= broken_phones
        
        # Action to execute
        # Phone.all.append(self)
        
phone1 = Phone('ackPhonev10', 500, 5, 1)
print(phone1.name)
print(phone1.calculate_total_price())
print(Phone.all)
print(Item.all)

# I have made some changes on @classmethod to change csv file in phone.py 
# module seperately. To check and see run the code below.
phone_module = __import__('phone')
phone_module.Phone.instantiate_from_csv()
print(phone_module.Phone.all)



############################ ENCAPSULATION #############################
'''
If we want to restrict the user to override some of the important attrs
such as name of attrs, we need to create read-only attrs, in other words
we need to use encapsulation to prevent this.
We will set up in initialization, and we should have error if someone tries
to override it.
We need to use @property decorator and then define a function with
attr name which takes the self parameter. And return some value.
When we try to reach it we should access it like a attribute 
(without paranthesis) not like a method. The magic comes exactly here. 
You cant override the function. @property decorator makes the function
(method) act like an attribute.(getter)
If we still want to change the value although it is private and unchangable,
we should use @instance_name.setter (setter) to make it available to set
a new value. 
If we use self._name it is still reachable but by convention we shouldn't change
its value but if we want to, we can. But if we restrict it totaly change it
from outside of the class we should define it with double underscore self.__name
It's not reachable like that from outside. If you want to change its value
i.e item1.__name = 'newname' you actually doesn't change it you actually define
a new attribute outside of the class.
__ dunder means that it can only accessable and callable inside the class. 
You cant access __sth outside the class it will give attr error.
Example:
obj.public
obj._protected
obj.__private  #Can't print this one, it will raise an AttibuteError
'''

item1 = Item('MyItem',850)
item1.name = "OtherItem" # We override the attr name here.
print(item1.name) # ->  "OtherItem"

# So lets create a new class and see the simple example
class Item2:
    def __init__(self,name, price, quantity =0):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    @property
    def read_only_name(self):
        return 'You can\'t change this'
    

item1 = Item2("NewItem",500)
print(item1.name, item1.read_only_name) # As you can see here we called 
# read_only_name here without paranthesis like attr.
#item1.read_only_name = "I will try to change this" # This will give error


# But if we want to do it at initialization process we'll do it like that
class Item:
    all = []
    pay_rate = 0.8 

    def __init__(self, name: str, price: float, quantity: int=0):
        assert isinstance(name, str), f'{name} is not str !'
        assert price >= 0, f'{price} is less than 0!'
        assert quantity >= 0, f'{quantity} is less than 0!'
        
        self._name = name # Add one underscore for instance's name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)
        
    @property #We set normal name like an attr which returns self._name
    def name(self):
        return self._name
    
    def calculate_total_price(self):
        return self.price * self.quantity
class Item:
    all = []
    pay_rate = 0.8 

    def __init__(self, name: str, price: float, quantity: int=0):
        assert isinstance(name, str), f'{name} is not str !'
        assert price >= 0, f'{price} is less than 0!'
        assert quantity >= 0, f'{quantity} is less than 0!'
        
        self._name = name # Add one underscore for instance's name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)
        
    @property #We set normal name like an attr which returns self._name
    def name(self):
        return self._name
    
    def calculate_total_price(self):
        return self.price * self.quantity
class Item:
    all = []
    pay_rate = 0.8 

    def __init__(self, name: str, price: float, quantity: int=0):
        assert isinstance(name, str), f'{name} is not str !'
        assert price >= 0, f'{price} is less than 0!'
        assert quantity >= 0, f'{quantity} is less than 0!'
        
        self._name = name # Add one underscore for instance's name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)
        
    @property #We set normal name like an attr which returns self._name
    def name(self):
        return self._name
    
    def calculate_total_price(self):
        return self.price * self.quantity
class Item:
    all = []
    pay_rate = 0.8 

    def __init__(self, name: str, price: float, quantity: int=0):
        assert isinstance(name, str), f'{name} is not str !'
        assert price >= 0, f'{price} is less than 0!'
        assert quantity >= 0, f'{quantity} is less than 0!'
        
        self._name = name # Add one underscore for instance's name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)
        
    @property #We set normal name like an attr which returns self._name
    def name(self):
        return self._name
    
    def calculate_total_price(self):
        return self.price * self.quantity
class Item:
    all = []
    pay_rate = 0.8 

    def __init__(self, name: str, price: float, quantity: int=0):
        assert isinstance(name, str), f'{name} is not str !'
        assert price >= 0, f'{price} is less than 0!'
        assert quantity >= 0, f'{quantity} is less than 0!'
        
        self._name = name # Add one underscore to instance's name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)
        
    @property #We set normal name like an attr which returns self._name
    def name(self):
        return self._name
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self): 
        self.price *= self.pay_rate 
        
    def __repr__(self):
        return  f'{self.__class__.__name__}("{self.name}",{self.price},\
{self.quantity})'
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            cls(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )
    
    @staticmethod
    def is_it_integer(number): 
        if isinstance(number, float):
            return number.is_integer()
        elif isinstance(number, int):
            return True
        else:
            return False
        
item1 = Item('MyItem',500)
print(item1.name)
#item1.name = "ChangeName" # this will give Attribute Error.

# However we actually know how to access and change the name (self._name)

item1._name = "ChangeName"
print(item1.name) # Changed succesfully. 


# To prevent the access from outside totally, we'll use __name 
class Item:
    all = []
    pay_rate = 0.8 

    def __init__(self, name: str, price: float, quantity: int=0):
        assert isinstance(name, str), f'{name} is not str !'
        assert price >= 0, f'{price} is less than 0!'
        assert quantity >= 0, f'{quantity} is less than 0!'
        
        self.__name = name # Add two underscore to instance's name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)
        
    @property 
    def name(self):
        return self.__name # Change here as well, double underscore
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self): 
        self.price *= self.pay_rate 
        
    def __repr__(self):
        return  f'{self.__class__.__name__}("{self.name}",{self.price},\
{self.quantity})'
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            cls(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )
    
    @staticmethod
    def is_it_integer(number): 
        if isinstance(number, float):
            return number.is_integer()
        elif isinstance(number, int):
            return True
        else:
            return False

item1 = Item("MyItem", 500)
#print(item1.__name) # This will give error
#item1.name = 'OtherItem' # This will give error
item1.__name = "OtherItem"
print(item1.name) # Name didnt change returns -> 'MyItem'
print(item1.__name) # Now it wont give error. It will return OtherItem
# just like we assigned a new value to new attr outside the class.


# Even though it is a private and encapsulated read-only attr we can still
# change it using special setter. By doing this we basicly say hey so I still
# want to set a new value for that name altough that is a property meaning read-
#only attribute
class Item:
    all = []
    pay_rate = 0.8 

    def __init__(self, name: str, price: float, quantity: int=0):
        assert isinstance(name, str), f'{name} is not str !'
        assert price >= 0, f'{price} is less than 0!'
        assert quantity >= 0, f'{quantity} is less than 0!'
        
        self.__name = name 
        self.price = price
        self.quantity = quantity

        Item.all.append(self)
        
    @property 
    def name(self):# Getter
        return self.__name 
    
    @name.setter # With this decorator we will be able to change it.
    # name.setter because name is the property function name
    def name(self, value):#Setter # The additional parameter 'value', 
    #refers to the new value that we will set to the name attr.
        self.__name = value
        
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self): 
        self.price *= self.pay_rate 
        
    def __repr__(self):
        return  f'{self.__class__.__name__}("{self.name}",{self.price},\
{self.quantity})'
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            cls(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )
    
    @staticmethod
    def is_it_integer(number): 
        if isinstance(number, float):
            return number.is_integer()
        elif isinstance(number, int):
            return True
        else:
            return False
    
item1 = Item("MyItem", 750)
item1.name = "OtherItem" # Thanks to @name.setter we are able to change
#without any Attribute Error
print(item1.name)


# Now we can restrict user with some rules with raise if the user want to
# change the name through the setter method.Example below
class Item:
    all = []
    pay_rate = 0.8 

    def __init__(self, name: str, price: float, quantity: int=0):
        assert isinstance(name, str), f'{name} is not str !'
        assert price >= 0, f'{price} is less than 0!'
        assert quantity >= 0, f'{quantity} is less than 0!'
        
        self.__name = name 
        self.price = price
        self.quantity = quantity

        Item.all.append(self)
        
    @property 
    def name(self):# Getter
        return self.__name 
    
    @name.setter
    def name(self, value): # Setter
        if len(value) > 10: # Restriction rule when change the name
            raise Exception('You cant do that it is too long!') 
        else:
            self.__name = value
        
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self): 
        self.price *= self.pay_rate 
        
    def __repr__(self):
        return  f'{self.__class__.__name__}("{self.name}",{self.price},\
{self.quantity})'
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            cls(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )
    
    @staticmethod
    def is_it_integer(number): 
        if isinstance(number, float):
            return number.is_integer()
        elif isinstance(number, int):
            return True
        else:
            return False

item1 = Item("MyItem", 500)
#item1.name = "OtherItemmmm" # will raise the exception, and give error



###################### Other Principles of OOP #########################
# Encapsulation
# Abstraction
# Inheritance
# Polymorphism

############################ ABSTRACTION ###############################
''' 
Abstraction is the concept of OOP that only shows the necessary attributes
and hides the unecessary information. Main purpose of abstraction it is
basically hiding the unnecessary detail from the users.
'''
# Lets assume that we will add send email method to our item class
# We will simulate the process not making a real mail sender.
# In order to send mail we should connect to the SMTP server, prepare
# a message body, send it etc...

class Item:
    all = []
    pay_rate = 0.8 

    def __init__(self, name: str, price: float, quantity: int=0):
        assert isinstance(name, str), f'{name} is not str !'
        assert price >= 0, f'{price} is less than 0!'
        assert quantity >= 0, f'{quantity} is less than 0!'
        
        self.__name = name 
        self.price = price
        self.quantity = quantity

        Item.all.append(self)
        
    @property 
    def name(self):
        return self.__name 
    
    @name.setter
    def name(self, value):
        if len(value) > 10: 
            raise Exception('You cant do that it is too long!') 
        else:
            self.__name = value
        
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self): 
        self.price *= self.pay_rate 
        
    def __repr__(self):
        return  f'{self.__class__.__name__}("{self.name}",{self.price},\
{self.quantity})'
    
    def connect(self,smtp_server='smtp_server'):# Only simulating the methods
        pass
    
    def prepare_body(self): # Only simulating the methods
        return f'''
    Hello Someone.
    We have {self.name} {self.quantity} times.
    Regards, Alicem Koyun
    '''
    
    def send(self): # Only simulating the methods
        pass
    
    def send_email(self):# Only simulating the methods
        self.connect()
        self.prepare_body()
        self.send()
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            cls(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )
    
    @staticmethod
    def is_it_integer(number): 
        if isinstance(number, float):
            return number.is_integer()
        elif isinstance(number, int):
            return True
        else:
            return False

item1 = Item("MyItem",750,6)
item1.send_email() # it sends it but we can still access the parts of 
# the sending email mechanism i.e down below
item1.connect() # We can access the mechanism, that is exactly what abstraction
# is about. Abstarction principle says to you that you should hide unnecessary
# information from the instances.
# To fix this we can add __ (dunder) to methods name. i.e.

class Item:
    all = []
    pay_rate = 0.8 

    def __init__(self, name: str, price: float, quantity: int=0):
        assert isinstance(name, str), f'{name} is not str !'
        assert price >= 0, f'{price} is less than 0!'
        assert quantity >= 0, f'{quantity} is less than 0!'
        
        self.__name = name 
        self.price = price
        self.quantity = quantity

        Item.all.append(self)
        
    @property 
    def name(self):
        return self.__name 
    
    @name.setter
    def name(self, value):
        if len(value) > 10: 
            raise Exception('You cant do that it is too long!') 
        else:
            self.__name = value
        
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self): 
        self.price *= self.pay_rate 
        
    def __repr__(self):
        return  f'{self.__class__.__name__}("{self.name}",{self.price},\
{self.quantity})'
    
    def __connect(self,smtp_server='smtp_server'): # __ added
        pass
    
    def __prepare_body(self):  # __ added
        return f'''
    Hello Someone.
    We have {self.name} {self.quantity} times.
    Regards, Alicem Koyun
    '''
    
    def __send(self): # __ added
        pass 
    
    def send_email(self): # we can access __things only inside the class
        self.__connect()
        self.__prepare_body()
        self.__send()
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            cls(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )
    
    @staticmethod
    def is_it_integer(number): 
        if isinstance(number, float):
            return number.is_integer()
        elif isinstance(number, int):
            return True
        else:
            return False

item1 = Item('MyItem', 750, 6)
item1.send_email()
#item1.connect() # This will give an attr error. Because we hide it using
# __connect and we can't acces it outside
#item1.__connect() # attr error cant accsess it from instances.

# Other example for Abstraction
from abc import ABC, abstractmethod


class AbstractVehicle(ABC):
    @abstractmethod
    def move(self):
        pass


class Car(AbstractVehicle):
    def move(self):
        print("Car is moving")

# AbstractVehicle cannot be instantiated,
# but Car, which implements the abstract method, can.




############################ POLYMORPHISM ##############################
'''
Poly= Many 
Morphism = Forms
Polymorphism refers to one single entity that we can use from multiple 
objects.
Polymorphism enables objects of different classes to be treated as objects of a common superclass. It’s about using a single interface to represent different underlying forms (data types).Polymorphism is essential for creating flexible and interchangeable objects that adhere to a common interface. This makes your code more modular and easier to scale.
'''

# len built-in function is the perfect example of Polymorphism we can
# use it to merge str and lists although they are different objects or 
# datatypes.
len('alicemkoyun') # for str -> 11
len(['ali', 'cem', 'koyun']) # for list -> 3

# If we want to use it in our class we can do it by inheriting the Item
# class in Phone class and using its methods such as apply_discount().
# Lets create different class and inherit from the Item class and show
# how it works.
class Keyboard(Item):
    pay_rate = 0.7 # Polymorphism in action. We override the attr from parent
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

item1 = Keyboard('Logitech',1000,3)

item1.apply_discount() # Also the beauty of Polymorphism to use parent class's
# methods on other instances or object also thanks to inheritance. That's why
# we will hear a lot the name of inheritance and polymorphism together. They are
# actually combined.
print(item1.price)

# Other Example For Polymorphism
class Rectangle:
    def draw(self):
        return "Drawing a rectangle"

class Circle:
    def draw(self):
        return "Drawing a circle"

def draw_shape(shape):
    print(shape.draw())


draw_shape(Rectangle())  # Output: Drawing a rectangle
draw_shape(Circle())     # Output: Drawing a circle




#################### OTHER OOP CONCEPTS AND MORE #######################
""" 
https://blog.devgenius.io/mastering-advanced-oop-concepts-in-python-theory-behind-oop-c9e87fb1697b

Building on our exploration of advanced class features in Python, this article delves into the theoretical foundations of Object-Oriented Programming (OOP). We’ll unravel essential OOP concepts such as Inheritance, Encapsulation, Polymorphism, Composition, Abstraction, Aggregation, and Association, and their practical applications in Python. Additionally, we’ll explore the Method Resolution Order (MRO) and key design patterns, providing you with a comprehensive understanding to enhance your Python programming skills.
"""

#######################      COMPOSITION      ########################
''' 
Composition involves constructing complex objects from simpler ones, rather than inheriting from a base or parent class. It provides flexibility in creating systems by connecting different parts together
Composition is preferable when objects need to be composed of features from multiple sources or when inheritance relationships are strained and don’t model the real-world accurately. It promotes loose coupling and better encapsulation, leading to more maintainable and flexible code.
'''
class Battery:
    def charge(self):
        return "Battery charging"

class Smartphone:
    def __init__(self):
        self.battery = Battery()

    def charge_phone(self):
        return self.battery.charge()


phone = Smartphone()
print(phone.charge_phone())  # Output: Battery charging




#######################       AGGREGATION         ######################
''' 
Aggregation is a special form of association that represents a “has-a” relationship between objects, where child objects can exist independently of the parent. It is typically used to model a whole-part relationship.

Aggregation is useful in scenarios where components can belong to different systems or have a life cycle independent of the parent object, such as components in a computer system.
'''
class Engine:
    def start(self):
        print("Engine starts")


class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()


engine = Engine()
car = Car(engine)
car.start()  # The Engine is part of the Car, but it's a separate, independent object



######################       ASSOCIATION      ##########################
''' 
Association represents a broad range of relationships between objects, including the use of one object within another. Unlike aggregation, association doesn’t imply ownership.

Association is often used in database relationships and in scenarios where objects need to interact but maintain their independence and life cycle, such as the relationship between students and teachers in a school system.
'''
class Professor:
    pass


class Department:
    def __init__(self, professor):
        self.professor = professor


# Here, Department is associated with Professor,
# but neither owns the other.



################### METHOD RESOLUTION ORDER (MRO) ######################
''' 
Understanding the Method Resolution Order (MRO) in Python is crucial when dealing with complex inheritance structures. It determines the order in which base classes are searched when executing a method. Proper comprehension of MRO can prevent common pitfalls in object-oriented design, especially in multiple inheritance scenarios.

The Concept of MRO
The MRO is a rule that Python follows to determine the order in which to search for base classes during method resolution. This becomes particularly important in multiple inheritance, where a class inherits from more than one parent class.

Python’s MRO Algorithm
Python uses the C3 linearization algorithm for MRO. This algorithm provides a consistent and predictable structure for method resolution, ensuring that a method is never repeated and that each parent is considered only once.
'''
# Understanding MRO with an Example
class A:
    def do_something(self):
        print("Method Defined In: A")


class B(A):
    def do_something(self):
        print("Method Defined In: B")


class C(A):
    def do_something(self):
        print("Method Defined In: C")


class D(B, C):
    pass


d = D()
d.do_something()  # Output: Method Defined In: B

#In this example, when calling d.do_something(), Python follows the MRO of class D, which is D, B, C, A. It executes the first do_something method it finds, which is in class B.


############## MRO and Super()
'''  
The super() function is used to call methods from a parent class. In the context of MRO, super() follows the MRO to determine the next class to look for the method.
'''
class Base:
    def __init__(self):
        print("Base initializer")


class A(Base):
    def __init__(self):
        super().__init__()
        print("A initializer")


class B(Base):
    def __init__(self):
        super().__init__()
        print("B initializer")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("C initializer")


c = C() #Base initializer-B initializer-A initializer-C initializer
# The output of this code demonstrates the order in which initializers are called, following the MRO of class C.

# If we try to visualize this it would look like a diamond as down below
'''
          Base
           |
          / \
         /   \
        A     B
         \   /
          \ /
           C

Bu diyagram, C sinifinin A ve B siniflarindan, A sinifinin da Base sinifindan miras aldiğini gösterir.

1- C sinifinin bir örneği oluşturulduğunda (c = C()), sira şu şekilde ilerler:

C sinifinin __init__ metodu çalişir.
super().__init__() ifadesi kullanilarak A sinifinin __init__ metodu çağrilir.

2- A sinifinin __init__ metodu içinde tekrar super().__init__() ifadesi bulunur. Bu ifade, siradaki üst sinif olan B sinifinin __init__ metodunu çağirir.

3- B sinifinin __init__ metodu içinde de super().__init__() ifadesi bulunur. Bu ifade, siradaki üst sinif olan Base sinifinin __init__ metodunu çağirir.

Bu nedenle, Base sinifinin __init__ metodu en başta çağrilir. Daha sonra sirasiyla B, A, ve C siniflarinin __init__ metodlari çağrilir. Bu siralama, önce Base, sonra B, ardindan A ve en son olarak C sinifinin __init__ metodunu çaliştirir.

MRO şu şekildedir: C -> A -> B -> Base. Bu siraya göre __init__ metodlari çağrilir.
'''

""" 
Best Practices and Common Pitfalls
Avoiding Diamond Inheritance: The “diamond problem” occurs in multiple inheritances when a class inherits from two classes that have a common base class. Proper understanding and application of MRO can help navigate this complexity.
Prefer Composition Over Complex Inheritance: When inheritance structures become too complex, consider using composition as an alternative to simplify relationships and improve code readability.
Consistent Use of super(): Ensure super() is used consistently in all methods that override parent methods. This helps maintain the integrity of the MRO and avoids unexpected behavior.
The MRO in Python is a powerful feature, but it requires careful handling to avoid complications in your object-oriented design. Understanding and applying the principles of MRO correctly can significantly enhance the robustness and clarity of your code, especially in complex inheritance scenarios.
"""
