'''
This module implements specialized container datatypes providing
alternatives to Python's general purpose built-in containers, dict,
list, set, and tuple.

* namedtuple   factory function for creating tuple subclasses with named fields
* deque        list-like container with fast appends and pops on either end
* ChainMap     dict-like class for creating a single view of multiple mappings
* Counter      dict subclass for counting hashable objects
* OrderedDict  dict subclass that remembers the order entries were added
* defaultdict  dict subclass that calls a factory function to supply missing values
* UserDict     wrapper around dictionary objects for easier dict subclassing
* UserList     wrapper around list objects for easier list subclassing
* UserString   wrapper around string objects for easier string subclassing
'''
import collections

#! Counter - Dict-like object

a = 'aaaaaaabbbbccc'
my_counter = collections.Counter(a)

print(my_counter.items()) # dict_items([('a', 7), ('b', 4), ('c', 3)])
print(my_counter.keys()) # dict_keys(['a', 'b', 'c'])
print(my_counter.values()) # dict_values([7, 4, 3])
print(my_counter.most_common(1)) # [('a', 7)]
print(my_counter.most_common(2)) # [('a', 7), ('b', 4)]
print(my_counter.most_common(3)) # [('a', 7), ('b', 4), ('c', 3)]
print(list(my_counter.elements())) # ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c']



#! namedtuple Class like lightweight object type

Point = collections.namedtuple('Point', 'x, y')
# Var name and Arg class name should be the same.
pt = Point(1, -4)
print(pt) # Point(x=1, y=-4)
print(pt.x) # 1
print(pt.y) # -4




#! OrderedDict - after Python 3.7 dicts are ordered anyway.

ordered_dict = collections.OrderedDict()
ordered_dict ['b'] = 2
ordered_dict ['c'] = 3
ordered_dict ['d'] = 4
ordered_dict ['a'] = 1
print(ordered_dict) # OrderedDict([('b', 2), ('c', 3), ('d', 4), ('a', 1)])



#! defaultdict Only difference is if we dont set a value for key

d = collections.defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['a'], d['b'], d['c']) # 1, 2, 0-> default val for int

d = collections.defaultdict(list)
d['a'] = 'a'
d['b'] = 'b'
print(d['a'], d['b'], d['c']) # a, b, []

#With a normal dict type it would raise a key error.




#! deque - Double ended queue, remove or add elements both ends.

d = collections.deque()

d.append(1)
d.append(2)
print(d) # deque([1, 2])

d.appendleft(3)
print(d) # deque([3, 1, 2])

d.pop()
print(d) # deque([3, 1])

d.popleft()
print(d) # deque([1])

d.clear()
print(d) # deque([])

d.extend([4, 5, 6])
print(d) # deque([4, 5, 6])

d.extendleft([7, 8, 9])
print(d) # deque([9, 8, 7, 4, 5, 6])

# Rotation
d_rotate = collections.deque()
d_rotate.extend([1,2,3,4,5])

d_rotate.rotate(1)
print(d_rotate) # deque([5, 1, 2, 3, 4])

d_rotate.rotate(2)
print(d_rotate) # deque([3, 4, 5, 1, 2])

# To negate the rotation direction
d_rotate.rotate(-2)
print(d_rotate) # deque([5, 1, 2, 3, 4])
d_rotate.rotate(-1)
print(d_rotate) # deque([1, 2, 3, 4, 5])