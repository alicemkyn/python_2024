############################# MODULES ##################################
'''
* Modules can import only in global scope, impossibe to import in 
funtions (local scope)

Frameworks > Libraries > Packages > Modules 
'''

# To find the source path of a module
import functools
print(functools.__file__)
# This __file__method doesn't work with sys module, because this module
# written in C language and it doesn't contain __file__ method.


# Common attributes in modules (PEP-Code Reusability)(Python Enhancement Proposals)
modules = ['os', 'random', 'sys', 'subprocess']

def intersection_modules(modules):
    set_list = [set(dir(__import__(module))) for module in modules]
    return set.intersection(*set_list)

print(intersection_modules(modules)) # That returns 5 common attributes
# {'__doc__', '__spec__', '__name__', '__loader__', '__package__'}

# __import__ function takes str as an argument and gives as the chance
# to import modules programatically. But it can be used only once after
# executing the line then module forgotten. If we want to do sth with this
# code snippet we should do it on the same line. e.g. uncomment the below :

#open('word_file.txt', 'a+').write('\nTest from modules.');__import__('subprocess').call(['open','-a', 'Sublime Text', 'word_file.txt'])



############################# __doc__ ##################################
'''
This one returns the docstrings of modules which are written at the top
of the module file. It is like about module specification.
'''
print(__import__('sys').__doc__)


########################### __name__ ###################################
'''
For example here modules.py files __name__ attr is '__main__' because we
create it, it is here and freshly edited right? we didn't import it any
where else in order to use. But if we import it from another file then 
its __name__ attr will be the file name, so 'modules'. Because it is im-
ported with this name because filename is modules.py.
'''

############################ __spec__ ##################################
'''
For name info and path info
'''
# at the beginning we imported functools
print(functools.__spec__.name)
print(functools.__spec__.origin)



############################## __all__ #################################
'''
It returns all the functions etc.. of module as a list.
'''
print(functools.__all__)



############################# __file__ #################################
'''
If the module has the this attr than it returns the installation path
of the modules
'''
print(functools.__file__)

# To see all the modules installed 
import pkgutil
import re 
modules = list(pkgutil.iter_modules())
for module in modules:
    pattern = re.compile(r'name=.+,')
    print(pattern.search(str(module)))
    print(str(module).split(',')[-2])
    
    
    

############################# PACKAGES #################################
'''
* Every package is a module but not every module is a package.
* Packages are consist of gathering multi modules.
* os.py is a module, yet collections are a package.
* Packages has __path__ attr.
* Packages repository is pypi.org, we can install it with using
'pip install'
* If package is manually downloaded, it can be processing using 
'python setup.py'
* dir() built_in function takes module as an argument.And we ca list
all the classes, variables, functions
'''



####################### IMPORTING FROM PACKAGES ########################
'''
1) import package.module
import urllib.request(urllib.request.urlopen())
2) from package import module
from urllib import request(request.urlopen())
3) from package.module import attr or method
from urllib.request import urlopen()
4) from package.module import *
from urllib.request import *
'''



######################### TO CREATE PACKAGES ###########################
''' 
All the py files inside a folder emerges the package and folders name 
is going to be the package name.
In Python 2.xx it was mandatory to put __init__.py file inside the
package folder but with Python 3.xx it is optional.
dir(package_name) > __path__ and __package__ indicates us that is a
package. and __package__ attr returns empty str.
'''
# How to import modules in the same folder.
# from . import module1 (. means is current folder)
# from . import module2 
# from .. import module3 (one level up from this folder)
# from ... import module4 (two level up from this folder)