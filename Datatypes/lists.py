############################### LIST ###################################
'''
- Mutable
- Ordered
- Indexable
- Can Contain Duplicates
* List slicing, List chunk = [StartIncluded:TillExcluded:StepDef=1!=0]
'''

# METHODS

# append(1_item) # ! adds to the end of the list

# extend(multiple_items)
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2)
print(l1) # [1, 2, 3, 4, 5, 6]

# insert(indexNo, item)
l1 = [0, 1, 2]
l1.insert(0, 5)
print(l1)  # [5, 0, 1, 2]
# OR
l1 = [0, 1, 2]
l1[0:0] = [5]
print(l1)

# remove(item)
l1 = ['apple', 'orange', 'pear', 'melon']
l1.remove('pear')
print(l1) # ['apple', 'orange', 'melon']

# reverse -> inplace
l1 = ['apple', 'orange', 'pear', 'melon']
l1.reverse()
print(l1) # ['melon', 'pear', 'orange', 'apple']
print(l1[::-1]) # back to the first case

# reversed() NOT inplace
print('reversed' in dir(__builtins__)) # True
l1 = [1, 2, 3, 4, 5]
print(list(reversed(l1))) # [5, 4, 3, 2, 1]
print(l1) # [1, 2, 3, 4, 5]

# pop() or pop(indexNo) 
# Without arg it will pop the last item in the list and returns it.
ls = [*range(5)]
a = ls.pop()
print(f'Popped item: {a}', f'List after : {ls} ') # Popped item: 4 List after : [0, 1, 2, 3] 

#sort() or sort(reverse=True) # Inplace
ls = [3,1,4,5,2]
ls.sort()
print(ls) # [1, 2, 3, 4, 5]
ls.sort(reverse=True)
print(ls) # [5, 4, 3, 2, 1]

# copy() # NOT Aliasing Creates Independent List 
l1 = [1, 2, 3, 4]
l2 = l1.copy()
print(l2)
# OR
l1 = [4, 3, 2, 1]
l2 = l1[:]
print(l2)
# OR
l1 = [7, 8, 9, 10]
l2 = list(l1)
print(l2)

# index(item) Show the index no of item
# count(item) Counts the given item piece in list

# clear() Clears the list items doesn't delete the list.
l1 = [1,2,3,4,5]
l1.clear()
print(l1) # []


# Some Mutation Examples
l = [1, 2, 3, 4]
l[0] = 5
print(l) # [5, 2, 3, 4]
l[1] += 2
print(l) # [5, 4, 3, 4]
l[0:3] = 30,40,60
print(l) # [30, 40, 60, 4]
l[0:3] = 30,40
print(l) # [30, 40, 4]
l[0:3] = 30,
print(l) # [30]