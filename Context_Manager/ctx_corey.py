'''
Ctx Man = We can use and manage resources exactly how we want to be managed.

1) We can create our context manager in Class with these dunder methods below:
__enter__ > set-up context manager
__exit__ > tear-down context manager

2) And also we can create our context manager using function.
We need to use @contextmanager decorator from contextlib module.
We can use this decorator to decorate the generator function.
'''


############################ CLASS EXAMPLE #############################
# Lets re-create with open() 
class Open_File():
    
    def __init__(self, filename, mod):
        self.filename = filename
        self.mod = mod
    
    def __enter__(self):
        self.file = open(self.filename, self.mod)
        return self.file
    
    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()


with Open_File('word_file.txt', 'a+') as f:
    f.write('Test from class type context manager')
    
print(f.closed) #True

# 1)Open_File('word_file.txt', 'a+') > __init__ method runs

# 2)with Open_File('word_file.txt', 'a+') as f: > __enter__method runs and
# sets new attr self.file and executes it with open() function then returns
# it (return self.file) 'as f' f sets to this return value always.
# e.g. f= return self.file
# In conclusion with Open_File('word_file.txt', 'a+') as f: with this line
# we call __init__ set attrs, we call __enter__ open the file with setted
# in __init__ and return the f value as setted to self.file.(like alias)

# 3) In indentation in with statement we can work with the file in anyway
# we want.

# 4) When the line hits the out of the indentation then __exit__ methods 
# works and closes the file.




########################## FUNCTION EXAMPLE ############################
from contextlib import contextmanager

@contextmanager
def open_file(file, mode):
    f = open(file, mode)
    yield f
    f.close()

with open_file('word_file.txt', 'a+') as t:
    t.write('\nTest from functional context manager')

print(t.closed) # True

# 1) In our function everything before the yield statement is going to 
# be equivalent to what our __enter__ method of our class was. So this 
# is going to be the setup of the context manager.
# open_file('word_file.txt', 'a+') we call here the function with these
# arguments in with statement. and the line before the yield statement,
# we do everything like in __enter__method. 

# 2) The yield is actually where the code within the with statement is 
# going to run. yield f is equivalent to return self.filename 
# f variable = yield f 

# 3) Everything after the yield statement is going to be equivalent to
# what was in the __exit__ method in our class.So this i going to be the
# teardown of context manager. f.close() works in __exit__ method.


### To handle the errors in funcional type context manager
@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode) 
        yield f
    finally:
        f.close()

with open_file('word_file.txt', 'a+') as f:
    f.write('\nTest from the error handling functional ctx man.')

print(f.closed) # True



############################ CD EXAMPLE ################################
# We will use os module additionally
import os

cwd = os.getcwd()
os.chdir('Context_Manager')
print(os.listdir())
os.chdir(cwd)

cwd = os.getcwd()
os.chdir('Modules')
print(os.listdir())
os.chdir(cwd)


# Lets do it with context manager
@contextmanager
def change_dir(destination):
    try: #set-up part
        cwd = os.getcwd()
        os.chdir(destination)
        yield # We are not working with any variables inside our ctx man.
    finally: #exit part (teardown)
        os.chdir(cwd)

with change_dir('Context_Manager'): # We didn't set the var after yield
# so we dont use 'as f'. 
    print(os.listdir()) # Here we can do anything then it automatically 
# returns back to the main cwd as we set in decorated change_dir function.

with change_dir('Modules'):
    print(os.listdir())
