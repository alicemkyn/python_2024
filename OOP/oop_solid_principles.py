""" 
SOLID stands for 5 principles:

[S]INGLE RESPONSIBILITY
[O]PEN/CLOSED
[L]ISKOV SUBSTITUTION
[I]NTERFACE SEGREGATION
[D]EPENDENCY INVERSION

Solid design principles first mentioned in a paper written in 2000 by a 
software engineer Robert Martin a.k.a. Uncle Bob
"""


####################### SINGLE RESPONSIBILITY #########################
class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

    def pay(self,payment_type, security_code):
        if payment_type == "debit":
            print("Processing debit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        elif payment_type == "credit":
            print("Processing credit payment type")
            print("Verifying securiy code : {security_code}")
            self.status = "paid"
        else:
            raise Exception(f"Unknown payment type: {payment_type}")

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
order.pay("debit", "0372846")

'''
We want classes and methods to have a single responsibility.Another way
to say it we want classess and methods to have high cohesion and low
coupling be responsible for only a single thing. And that ensures that 
you can reuse them much easier later on. In Order class payment part for
example shouldn't be the part of the order. So Order class has too many
responsibilities and we need to fix that by extracting the pay method and
putting it into a separate class. That has an advantage, if we want to add
another payment types such as ApplePay, Bitcoin etc... we don't have to 
change the Order class anymore we can do it in a payment processing side
of things. Lets do it and after that we can remove the pay method from
Order class.
'''

class PaymentProcessor:
    def pay_credit(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

    def pay_debit(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = PaymentProcessor()
processor.pay_debit(order,"0372846")
print(order.status)



############################ OPEN/CLOSED ###############################
'''
That means we want to write code that's open for extension.So we should
be able to extend the existing code with new functionality, but closed
for modification, we shouldn't need to modify the orginal code. Let take
PaymentProcessor class as an example. If we want to add an extra payment
method like Bitcoin, or Apple Pay we have to modify the PaymentProcessor.
So that violates the Open/Closed principle. So to fix this we need to
create a structure of classes and subclasses so we can just define a new
sub-class for each new payment type. In order to do that, we need to
refactor this payment processor class. Lets turn it into an abstract class
and create subclasses for each of the different payment types. We have to 
import ABC and @abstractmethod. For ABC check:
https://www.notion.so/TO-DO-s-FOR-PROGRAMMING-630c23b0f1ae47eab02125af9f644d7d?pvs=4
'''

from abc import ABC, abstractmethod

class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total
    
    
class PaymentProcessor(ABC): # Abstract class
    
    @abstractmethod # Method should be overriden
    def pay(self, order, security_code):
        pass
# We should inherit from the PaymentProcessor because it is AbstractClass
# we cant instantiate the class above. It will raise TypeError.


class DebitPaymentProcessor(PaymentProcessor): # Subclass  
    
    def pay(self, order, security_code): # We should override the method
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"
        
order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = DebitPaymentProcessor()
processor.pay(order,"0372846")
print(order.status)

# Now we dont violate the Open/Closed rule anymore. If we want to add
# new payment method we don't need to change the payment processor or
# the order anymore. i.e below

class PaypalPaymentProcessor(PaymentProcessor):
    
    def pay(self, order, security_code):
        print("Processing Paypal payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

print(order.total_price())
processor = PaypalPaymentProcessor()
processor.pay(order,"0372846")
print(order.status)



######################### LISKOV SUBSTITUTION ##########################
'''
If you have objects in a program, you should be able to replace those 
objects with instances of their subtypes, or subclasses. Without altering
the correctness of the programme.
'''

# Lets take a look again at this PayPalPaymentProcessor. Lets assume that
# Paypal doesnt work with security code but with email adresses. So if 
# we want to fix it, without changing anything in the code just simply 
# replacing the security_code sections with email adresses in the 
# PaypalPaymentProcessor class only, that means that,
# we are abusing the other payment types, in other words we are violating
# the Liskov Substitution principle.
# To fix this, we should set dependencies in initializer.

class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total
    
    
class PaymentProcessor(ABC): # Removed all security_code parameter.
    
    @abstractmethod 
    def pay(self, order):
        pass

class DebitPaymentProcessor(PaymentProcessor):   
    def __init__(self, security_code): # Initialized here
        self.security_code = security_code
        
    def pay(self, order):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code): # Init here
        self.security_code = security_code
    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"
        
class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_address): # Changed it to email_adress
        self.email_address = email_address
    def pay(self, order):
        print("Processing Paypal payment type")
        print(f"Verifying email adress: {self.email_address}")
        order.status = "paid"
        
order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = PaypalPaymentProcessor("hi@alicemkoyun.com")
processor.pay(order)




######################### INTERFACE SEGREGATION ########################
'''
Interface Segregation means that overall, it's better if you have several
specific interfaces as opposed to one general purpose interface. We split
one general interface so that subclasses can have more meaningful behaviour
without violating any principle.
'''

# Lets extend the Order class example and see how it works.

class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total
    
    
class PaymentProcessor(ABC): # General Purpose Interface
    
    @abstractmethod # We added 2 factor auth. here as an example
    def auth_sms(self,code):
        pass
    
    @abstractmethod 
    def pay(self, order):
        pass

class DebitPaymentProcessor(PaymentProcessor):   
    def __init__(self, security_code): 
        self.security_code = security_code
        self.verified = False
        
    def auth_sms(self,code): # We override the method from Abstract Base Class
        print(f"Verifying SMS code {code}")
        self.verified = True
        
    def pay(self, order):
        if not self.verified: # We check the verification here first
            raise Exception("Not Authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):# Imagine that this doesnt
# support SMS verification.
    def __init__(self, security_code): 
        self.security_code = security_code
    
    def auth_sms(self, code): # We dont implement anything but for the sake
# of Open/Closed principle we simply override the method and denoted that
# it not supported here.
        raise Exception("Credit card payments dont support SMS code authorization")
    # Actually this is also Liskov Substitution violation :)
    
    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"
        
class PaypalPaymentProcessor(PaymentProcessor): # This supports SMS auth.
    def __init__(self, email_address): 
        self.email_address = email_address
        self.verified = False
    
    def auth_sms(self, code):
        print(f"Verifying SMS code {code}")
        self.verified = True
    
    def pay(self, order): # We also check the verification here.
        if not self.verified:
            raise Exception("Not Authorized")
        print("Processing Paypal payment type")
        print(f"Verifying email adress: {self.email_address}")
        order.status = "paid"
        
# The fixation and modification above is violate the Interface Segregation
# principle because some of the PaymentProcesscor's subclasses doesn't support
# the SMS verification although we were told that we should create and override
# the auth_sms method for all subclasess by Abstract Base Class(ABC) - 
# PaymentProcesssor. So not to violate any of this principles lets create
# seperate interface for auth as a subclass of PaymentProcessor that adds SMS
# auth capabilities

class PaymentProcessor(ABC): 
    
    # @abstractmethod   # We no longer need this because of the segregation
    # def auth_sms(self,code):
    #     pass
    
    @abstractmethod 
    def pay(self, order):
        pass

class PaymentProcessor_SMS(PaymentProcessor):
    
    # We inherit from the parent class so we have now the pay method.
    # Lets add and auth_sms method here. 
    
    @abstractmethod # Magic is here. We can use @abstractmethod even if we
    # dont inherit from the ABC. Inheriting from ABC only shows that this 
    # is the Abstract Base Class (blueprint how to create subclasses).
    def aut_sms(self, code):
        pass
    
    # Now we have seperate class for subclasses that supports SMS auth.
    # If subclass doesn't support SMS auth then they have alternavite 
    # class(PaymentProcessor) that they can simply inherit from
    
    # Now lets design our classes compatible with Interface Seg.principle


class DebitPaymentProcessor(PaymentProcessor_SMS):# Change the inheritance
    
# ABC > PaymentProcessor > PaymentProcessor_SMS > DebitPaymentProcessor

    def __init__(self, security_code): # For Liskov Substitution 
        self.security_code = security_code
        self.verified = False
        
    def auth_sms(self,code): # From PaymentProcessor_SMS class
        print(f"Verifying SMS code {code}")
        self.verified = True
        
    def pay(self, order): # From PaymentProcessor class
        if not self.verified: 
            raise Exception("Not Authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor): # We inherit from other 
# general class because we assume that this payment method doesn't support
# SMS verification or authorization.
    def __init__(self, security_code): 
        self.security_code = security_code
    
    # def auth_sms(self, code): # We dont need this weird method with Raise anymore
    #     raise Exception("Credit card payments dont support SMS code authorization")

    
    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"
        
class PaypalPaymentProcessor(PaymentProcessor_SMS): # This supports SMS auth.
    def __init__(self, email_address): 
        self.email_address = email_address
        self.verified = False
    
    def auth_sms(self, code):
        print(f"Verifying SMS code {code}")
        self.verified = True
    
    def pay(self, order): 
        if not self.verified:
            raise Exception("Not Authorized")
        print("Processing Paypal payment type")
        print(f"Verifying email adress: {self.email_address}")
        order.status = "paid"
        
        
# Instead of using and creating huge inheritance tree we can also use Composition.
# Lets create seperate class that handles the authentication
# For Composition and other advanced OOP concepts check the link below:
# https://medium.com/@ramanbazhanau/mastering-advanced-oop-concepts-in-python-theory-behind-oop-c9e87fb1697b

class Order:
    
    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


class SMSauth: # Composition class 
    
    def __init__(self):
        self.authorized = False    
        
    def verify_code(self,code):
        print(f"Verifying code {code}")
        self.authorized = True
    
    def is_authorized(self) -> bool:
        return self.authorized


class PaymentProcessor(ABC): 
    
    @abstractmethod 
    def pay(self, order):
        pass
    
# Removed the PaymentProcesscor_SMS class
    
class DebitPaymentProcessor(PaymentProcessor):
    
    def __init__(self, security_code, authorizer: SMSauth): # authorizer passed
        self.authorizer = authorizer
        self.security_code = security_code
        
    def pay(self, order): 
        if not self.authorizer.is_authorized(): 
            raise Exception("Not Authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"
        

class CreditPaymentProcessor(PaymentProcessor): 
    
    def __init__(self, security_code): 
        self.security_code = security_code
    
    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"
        
        
class PaypalPaymentProcessor(PaymentProcessor):
    
    def __init__(self, email_address,authorizer: SMSauth): # auth passed
        self.email_address = email_address
        self.authorizer = authorizer
    
    def pay(self, order): 
        if not self.authorizer.is_authorized():
            raise Exception("Not Authorized")
        print("Processing Paypal payment type")
        print(f"Verifying email adress: {self.email_address}")
        order.status = "paid"

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
authorizer = SMSauth()
processor = PaypalPaymentProcessor("hi@alicemkoyun.com", authorizer)
authorizer.verify_code(31231)
processor.pay(order)




######################### DEPENDENCY INVERSION #########################
'''
Dependency inversion means that we want our classes to depend on
abstractions and not on concrete subclasses.
In this code this is currently an issue:

class DebitPaymentProcessor(PaymentProcessor):
    
    def __init__(self, security_code, authorizer: SMSauth):
        self.authorizer = authorizer
        self.security_code = security_code

Because the payment processor are depending on specific authorizer: SMSauth
To solve that we should create another abstract authorizer class that you 
pass to the payment processors
'''
class Authorizer(ABC): # Created abstract class to pass as a paramater to 
# subclasses
    
    @abstractmethod
    def is_authorized(self):
        pass
    
    
class SMSauth(Authorizer): # Now it is a subclass of Authorizer
    
    def __init__(self):
        self.authorized = False    
        
    def verify_code(self,code):
        print(f"Verifying code {code}")
        self.authorized = True
    
    def is_authorized(self) -> bool:
        return self.authorized

# Lets create another class that checks whether you're robot 

class NotARobot(Authorizer):
    def __init__(self):
        self.authorized = False

    def not_a_robot(self):
        print("Are you a robot?")
        self.authorized = True
        
    def is_authorized(self) -> bool:
        return self.authorized

class PaymentProcessor(ABC): 
    
    @abstractmethod 
    def pay(self, order):
        pass
    
    
class DebitPaymentProcessor(PaymentProcessor):
    
    def __init__(self, security_code, authorizer: Authorizer):# auth passed and
# Type changed from SMSauth to Authorizer(abstract class)
        self.authorizer = authorizer
        self.security_code = security_code
        
    def pay(self, order): 
        if not self.authorizer.is_authorized(): 
            raise Exception("Not Authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"
        

class CreditPaymentProcessor(PaymentProcessor): 
    
    def __init__(self, security_code): 
        self.security_code = security_code
    
    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"
        
        
class PaypalPaymentProcessor(PaymentProcessor):
    
    def __init__(self, email_address,authorizer: Authorizer): # auth passed
        self.email_address = email_address
        self.authorizer = authorizer
    
    def pay(self, order): 
        if not self.authorizer.is_authorized():
            raise Exception("Not Authorized")
        print("Processing Paypal payment type")
        print(f"Verifying email adress: {self.email_address}")
        order.status = "paid"

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
#authorizer = SMSauth()
authorizer = NotARobot()
processor = PaypalPaymentProcessor("hi@alicemkoyun.com", authorizer)
authorizer.not_a_robot()
processor.pay(order)

# DEPENDENCY INJECTION IS BAD
# DEPENDENCY INVERSION IS PERFECT