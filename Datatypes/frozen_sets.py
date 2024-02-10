########################### FROZEN SET ################################
'''
As mentioned before, we can change the sets, they are mutable. And add(), remove(), update() methods prove it. If we need an immutable set
then we should initialize it not with set() but frozenset().
'''

# Example
frozen = frozenset(['apple', 'pears'])
print(dir(frozen)) 
# It will return the methods but there won't be add(), remove() or update().
# Only difference sets are mutable, frozensets are immutable. Other
# methods and attrs are the same.
