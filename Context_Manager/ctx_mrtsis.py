'''
Context Manager (Baglam Yoneticisi) Efficiently Managing Resources

* Remember __enter__ and __exit__ magic methods
* __exit__ ends the process or closes the file no matter what happens

Some examples to remember the process:

with open('/path/to/file.txt', 'r', encoding='utf8') as f:
    for line in f:
        print(line)

# OR

f = open('/path/to/file.txt', 'r', encoding='utf8')
for line in f:
    print(line)
f.close() # must remember to close f

# OR

try:
    f = open('/path/to/file.txt', 'r', encoding='utf8')
    for line in f:
        print(line)
finally:
    f.close() # runs no matter what happens
'''

class Word:
    def __init__(self):
        self.name = 'deneme'
        self.word_file = open('word_file.txt', 'a+')
        print('init run')
    
    def __enter__(self):
        print('enter run')
        #return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb, sep=', ')
        if exc_type is ValueError:
            print('Word has unconvertable chars')
            self.word_file.close()
            print(self.word_file.closed)
            return True # with this line error can't prevent the flow
        self.word_file.close()
        print(self.word_file.closed)
        print('exit run')


        
with Word() as w:
    #print(w.name) #AttributeError: 'NoneType' object has no attribute 'name'
    #Because we didn't return self in __enter__ method.
    print('with block')
# init run
# enter run
# with block 
# None, None, None
# True
# exit run

with Word() as w:
    raise ValueError('Ooops... Something went wrong.')
    print('with block')
# init run
# enter run
# <class 'ValueError'>, Ooops... Something went wrong., <traceback object at 0x102a3b080>
# Word has unconvertable chars
# True


