from item import Item
from phone import Phone

Item.instantiate_from_csv()
print(Item.all)
Phone.instantiate_from_csv()
print(Phone.all)



item1 = Item("MyItem",750)
item1.name = "OtherItem" # we override the name attribute here

print(item1.name)
print(item1.is_it_integer(5))


####### @classmethod vs @statitcmethod
class MyClass:
    @staticmethod
    def my_static_method():
        print("This is a static method.")
    @classmethod
    def my_class_method(cls):
        print(f"This is a class method of {cls}")

obj = MyClass()
obj.my_static_method() # This is NOT convention
MyClass.my_static_method() # This is convention

MyClass.my_class_method() # This is convention
obj.my_class_method() # This is also a convention

class MyClass_2(MyClass):
    pass

obj_2 = MyClass_2()
obj_2.my_class_method()
MyClass_2.my_class_method()



####### Difference ######

class MyClass1:
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    def from_classmethod(cls):
        return cls(cls.class_variable)

    @staticmethod
    def from_staticmethod():
        return MyClass1(MyClass1.class_variable)

# ClassMethod üzerinden çağrıldığında bir örnek oluşturulur
obj1 = MyClass1.from_classmethod()
print(obj1.instance_variable)  # "I am a class variable"

# StaticMethod üzerinden çağrıldığında da bir örnek oluşturulur
obj2 = MyClass1.from_staticmethod()
print(obj2.instance_variable)  # "I am a class variable"


class MyClass2(MyClass1):
    class_variable = "I am a class variable from MyClass2"


inst1 = MyClass2.from_classmethod()
print(inst1.instance_variable) # "I am a class variable from MyClass2"
inst2 = MyClass2.from_staticmethod()
print(inst2.instance_variable) # "I am a class variable"



###### MetaClass Ornegi #######
class FooMeta(type):
    def __new__(cls, name, bases, dct):
        assert "bar" in dct, 'bar class attr. tanimla'
        assert isinstance(dct['bar'],list), f'bar lst olmali {dct["bar"]} degil'
        return super().__new__(cls,name,bases,dct)

class MyClass(metaclass=FooMeta):
    bar = []
    def __init__(self):
        pass

# cls = FooMeta
# name = MyClass
# bases = whether there is an inheritance, tuple ()
# dct = MyClass.__dict__


##### Singleton ornegi
class Singleton:
    _instance = None

    @staticmethod
    def getInstance():
        if Singleton._instance == None:
            Singleton()
        return Singleton._instance

    def __init__(self):
        if Singleton._instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton._instance = self

s = Singleton.getInstance()
print(s)

m = Singleton.getInstance()
print(m is s)
print(m == s)
print(isinstance(m and s, Singleton))