'''
- Mutable
- Unordered
- Unindexable
- Can contain duplicate of values NOT KEYS
- dict = {'key' : 'value'}
- dict[key] -> Returns the value
- dict[key] = value -> Assigns the value
- Dict keys must be uniques.
- Dict keys must be immutable. If use tuples as key, then it must 
contain only immutable items inside, such as str, int, or other tuples,inside the tuple.
- Mutable -> Unhashable
- Immutable -> Hashable
'''

# Dict Comprehensions
names = ['cem', 'ali', 'koyun']
dictionary = {i:len(i) for i in names}
print(dictionary) # {'cem': 3, 'ali': 3, 'koyun': 5}

# Dictionary Methods
# keys()
dic = {'a':0, 'b':1, 'c':2, 'd':3}
print(dic.keys()) # dict_keys(['a', 'b', 'c', 'd'])

l = list(dic.keys())
print(l) # ['a', 'b', 'c', 'd']


# values() -> Same ex above and same result. But returns values instead
seq = ''.join([str(i) for i in dic.values()])
print(seq) # '0123'


# items() -> Same example
print(dic.items()) # dict_items([('a', 0), ('b', 1), ('c', 2), ('d', 3)])

for key, value in dic.items():
    print('{} = {}'.format(key, value)) # a = 0 b = 1 c = 2 d = 3


# get()
eng = {
    'dil':'language',
    'bilgisayar':'computer',
    'masa':'table'
    }

sorgu = input('Anlamini ogrenmek istedigin kelimeyi yaz:\t')
print(eng.get(sorgu, 'Bu kelime veritabaninda yok.'))


# clear() Deletes the keys and values not the dict. Like in list.
dc = {'alicem':'koyun', (1,4,5):[11,44,55]}
dc.clear()
print(dc) # {}


# copy() 
'''
To not affect the original dict, use this method. Because dicts are
Mutable datatypes. This method works same as in lists.
'''
d1 = {1:2, 3:4, '5':6.6}
d2 = d1.copy()
d1[1]=11
print(d1) # {1: 11, 3: 4, '5': 6.6}
print(d2) # {1: 2, 3: 4, '5': 6.6}


# fromkeys()
'''
- Doesn't work on dictionaries.
- It is used for creating dictionaries.
'''
employees = ('Tej', 'Singh', 'Preet')
dct_employees = dict.fromkeys(employees)
print(dct_employees) # {'Tej': None, 'Singh': None, 'Preet': None}
# OR
dct_emp_adress = dict.fromkeys(employees, 'Bengal')
print(dct_emp_adress) # {'Tej': 'Bengal', 'Singh': 'Bengal', 'Preet': 'Bengal'}


# pop()
'''
- Cant use without parameter NOT as in list.
- Use key as a parameter.
- It deletes the key and returns the value.
- If key doesn't exist, will give error.
- But like in get method, we can set the error message.
'''
eg = {'a': 0, 'b': (0,1,2), 'c' : [11,22,33,44]}
dlt = eg.pop('c')
print(f'Deleted keys value is : {dlt}') # Deleted keys value is : [11, 22, 33, 44]
print(eg) # {'a': 0, 'b': (0, 1, 2)}
print(eg.pop('d', 'No such key in dict.')) # No such key in dict.


# popitem()
'''
- Possible to use without parameter.
- Deletes the last added item.
'''
abc = {11:22, 33:44, 55:66}
popped = abc.popitem()
print(popped) # (55, 66)
print(abc) # {11: 22, 33: 44}


# setdefault()
'''
- Adds key value pair if key doesn't exist in the list. Doesn't update
the value of the key if included.
- If key exists returns its value and doesn't update.
'''
dc_set = {'a':0, 'b': 1, 'c' : 2,}
print(dc_set.setdefault('b', (4,5,6))) # 1


# update()
stock = {'apple':5, 'pears': 10, 'cheese' : 6}
new_stock = {'apple': 3, 'pears': 20, 'cheese': 8, 'salami': 4, 'steak': 10}
stock.update(new_stock)
print(stock)
# {'apple': 3, 'pears': 20, 'cheese': 8, 'salami': 4, 'steak': 10}


# EXAMPLE
files = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}

# Output : {'Stan':['Code.py'], 'Randy': ['Input.txt', 'Output.txt']}

# Solution
def func(files):
    d = {}
    for i, j in files.items():
        if j in d:
            d[j].append(i)
        else:
            d[j] = [i]
    return d

print(func(files)) 
# {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}


