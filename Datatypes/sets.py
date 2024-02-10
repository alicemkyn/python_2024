'''
- Mutable
- Unindexable
- No Duplicates
- Items should be immutable
- Unordered
- s = set()
list = [key, value for key, value in dict.items()]
s = set(liste) - Parameters should be iterable
- s1 - s2 = s1.difference(s2)
- s1 | s2 = s1.union(s2)
- s1 & s2 = s1.intersection(s2)
- (s1 - s2) & (s2 - s1) # symmetric_difference()
'''

# Example
ls = ['1', '2', '3', '1', '2', '3']
for i in set(ls):
    print('There are {} pieces of {}'.format(ls.count(i), i))
'''
Output:
There are 2 pieces of 3
There are 2 pieces of 2
There are 2 pieces of 1
'''

# Set Comprehensions
import random
ls = [random.randint(0, 1000) for i in range(1000)]
st = {i for i in ls if i < 100}
print(st)


########################## SET METHODS ################################
# clear() Empties the set
km = set('alicem')
print(km) # {'a', 'i', 'e', 'l', 'c', 'm'}
km.clear()
print(km) # set()


# copy() Copies the set. Same in list
km = set('kahramanmaras')
backup = km.copy()
print(km) # {'h', 'r', 'n', 'a', 'k', 's', 'm'}
print(backup) # {'h', 'r', 'a', 'k', 'n', 's', 'm'}


# add() Takes only one argument
s = set(['apple', 'banana', 'cherry'])
s.add('melon') # This state is proof that sets are mutable.
print(s) # {'cherry', 'banana', 'apple', 'melon'}


# difference()
k1 = set([1,2,3,4,5])
k2 = set([3,4,2,10])
print(k1.difference(k2)) # {1, 5}
# OR
print(k1 - k2) # {1, 5} # We CAN'T use plus for merging two sets


# difference.update() Updates the set according to the result.
k1 = set([1,2,3])
k2 = set([1,3,5])
k1.difference_update(k2)
print(k1) # {2}


# discard()
'''
Deletes the given parameter from the set. If doesn't exist, doesn't
give any error message and stop the program flow.
'''
k1 = {1,2,3,4,5}
k1.discard(3)
k1.discard(14)
print(k1) # {1, 2, 4, 5}


# remove() Same as discard(). But this gives error if cant find the arg

# union()
a = set([2, 4, 6, 8])
b = set([1, 3, 5, 7])
c = a.union(b)
print(c) # {1, 2, 3, 4, 5, 6, 7, 8}
# OR
print(a | b) # {1, 2, 3, 4, 5, 6, 7, 8}


# intersection()
k1 = set([1, 2, 3, 4])
k2 = set([1, 3, 5, 7])
k3 = k1.intersection(k2)
print(k3) # {1, 3}
# OR
print(k1 & k2) # {1, 3}
# Example
tr = {"ş,ç,ö,ğ,ü,ı,Ş,Ç,Ö,Ü,Ğ,I "}
password = input('Password:\t')
if set(tr) & set(password):
    print('Don\'t Use Turkish Characters!')
else:
    print('Authenticated. Please wait...')

# intersection_update()
k1 = set([1, 2, 3])
k2 = set([1, 3, 5])
k1.intersection_update(k2)
print(k1) # {1, 3}


# issubset() -> bool
a = set([1, 2, 3])
b = set([0, 1, 2, 3, 4, 5])
print(a.issubset(b)) # True


# isdisjoint() - Ayrik Kume Iki kumenin kesisim kumesi bosmu ?
a = set([1, 2, 3])
b = set([2, 4, 6])
print(a.isdisjoint(b)) # False

a = set([1, 3, 5])
b = set([2, 4, 6])
print(a.isdisjoint(b)) # True - No common item


# issuperset() Same as subset but opposite.
a = set([1, 2, 3])
b = set([0, 1, 2, 3, 4, 5])

print(b.issuperset(a)) # True
print(a.issuperset(b)) # False


# update()
st = set(['apple', 'pears', 'kebap'])
new = [1, 2, 3]
st.update(new)
print(st) # {1, 2, 3, 'kebap', 'apple', 'pears'}


# symmetric_difference()
a = set([1, 2, 5])
b = set([1, 4, 5])

a.difference(b) # {2}
b.difference(a) # {4}

print(a.symmetric_difference(b)) # {2, 4}


# symmetric_difference_update()
a = set([1, 2, 5])
b = set([1, 4, 5])

a.symmetric_difference_update(b)
print(a) # {2, 4}


# pop() Deletes random item and returns it.
a = set(['apple', 'pears', 'kebap'])
print(a.pop()) # apple
print(a) # {'kebap', 'pears'}

