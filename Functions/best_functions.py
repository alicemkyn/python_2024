# reduce()
from functools import reduce

print(reduce(lambda x,y : x + y, [12, 18, 20, 10])) # 60
'''
it adds first 12 + 18 = 30 then,
30 + 20 = 50,
50 + 10 = 60

This function very useful for factorial calculation.
'''


# filter()
'''
Works if True or False
Filters the False and returns the True statements.
'''

print(list(filter(lambda x: x % 2 == 0, [*range(11)])))
# [0, 2, 4, 6, 8, 10]

dromes = ('demigod', 'rewire', 'madam', 'freer', 'anutforajaroftuna', 'kiosk')
palindromes = list(filter(lambda x : x==x[::-1], dromes))
print(palindromes) # ['madam', 'anutforajaroftuna']

scores = [66, 80, 90, 68, 59, 76, 60, 88, 74, 81, 65]
over_85 = list(filter(lambda x: x >= 85, scores))
print(over_85) # [90, 88]



# map()
print(list(map(lambda x: 2 ** x, [1,2,3,4,5]))) # [2, 4, 8, 16, 32]

my_pets = ['alfred', 'tabitha', 'william']
print(list(map(lambda x: x.upper(), my_pets))) # ['ALFRED', 'TABITHA', 'WILLIAM']
print(list(map(str.upper, my_pets))) # ['ALFRED', 'TABITHA', 'WILLIAM']

rect_width = [(3, 4), (10, 3), (5, 6), (1, 9)]
rect_area = list(map(lambda x: x[0] * x[1], rect_width))
print(rect_area) # [12, 30, 30, 9]


# zip()
my_strings = ['a', 'b', 'c', 'd', 'e']
my_nums = [1, 2, 3, 4, 5]
result = list(zip(my_strings, my_nums))
print(result) # [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]

my_strings = ['a', 'b', 'c', 'd']
result = list(zip(my_strings, my_nums))
print(result) # [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

for i, j in result:
    print(i, j)


# enumerate()
ls = ['Apple', 'Pears', 'Banana', 'Cherry']
print(list(enumerate(ls))) 
# [(0, 'Apple'), (1, 'Pears'), (2, 'Banana'), (3, 'Cherry')]
print(list(enumerate(ls,1))) 
#[(1, 'Apple'), (2, 'Pears'), (3, 'Banana'), (4, 'Cherry')]

for i,j in list(enumerate(ls)):
    if i % 2 == 0:
        print(j) # Apple Banana
    
