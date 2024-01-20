import logging
import os
logging.basicConfig(level=logging.DEBUG, format='%(message)s')
lg = logging.debug


# 1
lg(os.name) # posix

# 2
lg(os.sep) # /
ls = ['months', 'july', 'test']
lg(os.sep.join(ls)) # months/july/test

# 3
lg(os.getcwd()) # /Users/alicemkoyun/Programming

# 4
os.chdir('/Users/alicemkoyun/') # Changes the directory
lg(os.getcwd()) # /Users/alicemkoyun

# 5 
lg(os.listdir(os.chdir('/Users/alicemkoyun/Programming/Os_Module/'))) # ['os_module.py']

# 6
lg(os.curdir) # .
lg(os.listdir(os.curdir)) # ['os_module.py']

# 7
lg(os.pardir) # ..  (Parent Directory)(One level up folder)
lg(os.listdir(os.pardir)) # ['application.db', 'word_file.txt', '.DS_Store', 'Context_Manager', 'Datetime', 'old_repo', 'OOP', 'Os_Module', 'test.py', 'Regex', '.gitignore', 'SQLite3', 'Sptfy2Ytb', 'Functions', '.git', 'Modules', 'Logging', 'Git']

# 8
#os.startfile('/../word_file.txt') # This opens the files but works only in Windows

# 9 
#os.mkdir('/Users/alicemkoyun/Programming/alicem') # Creates folder to given direction. If some of the folder of given path is not exists it will raise an error.

# 10
#os.mkdirs('Users/alicemkoyun/Programming/alicem) # Even though non of them is exists, it will create every folder in given path.

# 11
#os.rename() # e.g. to rename the folder demo to test
#os.rename('demo', 'test')

# 12 
#os.replace() # works same as os.rename() no difference at all.

# 13
#os.remove('file_name') # Use it carefully because it deletes completely without asking for permission.

# 14
#os.rmdir() # If the folder is empty that removes the folder if not empty, it will give error.

# 15
#os.rmdirs() # If all the folders are empty in given path name, it removes everything including the parent directory.
#os.rmdirs('/main/folder1/folder2/folder3')

# 16
#os.stat() -> We used in datetime module, it provides us to get information about the given file such as size, creation date, change date, access date.
f = os.stat('/Users/alicemkoyun/Programming/word_file.txt')
lg(dir(f))
'''
Output:
st_atime = Last access date
st_ctime = Creation date
st_mtime = Last change date
st_size = Size
'''
lg(f.st_atime) # 1705320972.797712
lg(f.st_mtime) # 1705320971.314912
lg(f.st_ctime) # 1705320971.4083483
lg(f.st_size) # 160

# 17
#os.system() # That provides us to run system commands or programs inside the Python.
#os.system('cmatrix')

# 18
lg(os.urandom(12)) # b'\xa1\x97Nh_\x17\xd7\xbe\xff\xc2\xebP'
# Creates random byte string(12 byte) #It can be used in cryptographic works or creating passwords

# 19
#os.walk('path') # It gives everything in the given path, returns tuple with 3 items. ('main_path', [folder list], [file list in path])
# If we need the file list only:
for path, folders, files in (os.walk('/Users/alicemkoyun/Programming')):
    lg(files)
'''
output:
...
['main']
['subprcss.py', 'modules.py']
['logging_.py', 'basic.log', 'log2papertrail.py']
['git.ipynb', '.DS_Store']
['index.html', '.DS_Store', 'README.md']
...

'''

# 20
lg(os.environ) # returns the dict of environment variables in Operating System

for k,v in os.environ.items():
    print(k.ljust(15), v)

lg(os.environ['HOME']) # /Users/alicemkoyun
lg(os.environ['USER']) # alicemkoyun

# 21
# os.path #This is an attibute and it contains other attrs and methods

# os.path.abspath() # returns the path of a file
lg(os.path.abspath('os_module.py')) # /Users/alicemkoyun/Programming/Os_Module/os_module.py

# os.path.dirname() # returns only parents of file
lg(os.path.dirname('/Users/alicemkoyun/Programming/Os_Module/os_module.py')) # /Users/alicemkoyun/Programming/Os_Module
lg(os.path.dirname(os.path.abspath('os_module.py'))) # /Users/alicemkoyun/Programming/Os_Module

# os.path.exists() # checks if path or file exists. Returns bool
lg(os.path.exists('/Users/alicemkoyun/Programming/Os_Module/os_module.py')) # True

# os.path.expanduser() # gives the user's path 
lg(os.path.expanduser('~')) # /Users/alicemkoyun

# os.path.isdir() # If given parameter is a directory -> True
lg(os.path.isdir('/Users/alicemkoyun')) # True

# os.path.isfile() # if given parameter is a file -> True
lg(os.path.isfile('/Users/alicemkoyun/Programming/word_file.txt')) # True

# os.path.join() # This method creates the convinient paths according the OS with given parameters.
#os.path.join(parentpath, folder, 'file_name') -> /parentpath/folder/file_name.ext

# os.path.split() # This method seperates the last path elements from the other part returns tuple object.
lg(os.path.split('/Users/alicemkoyun/Programming')) # ('/Users/alicemkoyun', 'Programming')

# os.path.splitext() # It uses for seperating the file name and its extension from each other.
lg(os.path.splitext('word_file.txt')) # ('word_file', '.txt')

