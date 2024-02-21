'''
- PrettyPrinter
- isreadable
- isrecursive
- pformat
- pp
- pprint
- re
- saferepr


Support to pretty-print lists, tuples, & dictionaries recursively.

Very simple, but useful, especially in debugging data structures.

Classes
-------

PrettyPrinter()
    Handle pretty-printing operations onto a stream using a configured
    set of formatting parameters.

Functions
---------

pformat()
    Format a Python object into a pretty-printed representation.

pprint()
    Pretty-print a Python object to a stream [default is sys.stdout].

saferepr()
    Generate a 'standard' repr()-like value, but protect against recursive
    data structures.
'''


import pprint
import os

t_size = os.get_terminal_size()
w = t_size.columns

print(globals())
print('-' * w)
pprint.pprint(globals())