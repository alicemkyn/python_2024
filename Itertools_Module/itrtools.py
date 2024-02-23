import itertools
import os
'''
#! Very quick and memory efficient way creating iterators.

NAME
    itertools - Functional tools for creating and using iterators.

DESCRIPTION
    Infinite iterators:
    count(start=0, step=1) --> start, start+step, start+2*step, ...
    cycle(p) --> p0, p1, ... plast, p0, p1, ...
    repeat(elem [,n]) --> elem, elem, elem, ... endlessly or up to n times
    
    Iterators terminating on the shortest input sequence:
    accumulate(p[, func]) --> p0, p0+p1, p0+p1+p2
    chain(p, q, ...) --> p0, p1, ... plast, q0, q1, ...
    chain.from_iterable([p, q, ...]) --> p0, p1, ... plast, q0, q1, ...
    compress(data, selectors) --> (d[0] if s[0]), (d[1] if s[1]), ...
    dropwhile(pred, seq) --> seq[n], seq[n+1], starting when pred fails
    groupby(iterable[, keyfunc]) --> sub-iterators grouped by value of keyfunc(v)
    filterfalse(pred, seq) --> elements of seq where pred(elem) is False
    islice(seq, [start,] stop [, step]) --> elements from seq[start:stop:step]
    pairwise(s) --> (s[0],s[1]), (s[1],s[2]), (s[2], s[3]), ...
    starmap(fun, seq) --> fun(*seq[0]), fun(*seq[1]), ...
    tee(it, n=2) --> (it1, it2 , ... itn) splits one iterator into n
    takewhile(pred, seq) --> seq[0], seq[1], until pred fails
    zip_longest(p, q, ...) --> (p[0], q[0]), (p[1], q[1]), ...
    
    Combinatoric generators:
    product(p, q, ... [repeat=1]) --> cartesian product
    permutations(p[, r])
    combinations(p, r)
    combinations_with_replacement(p, r)

CLASSES
    builtins.object
        accumulate
        chain
        combinations
        combinations_with_replacement
        compress
        count
        cycle
        dropwhile
        filterfalse
        groupby
        islice
        pairwise
        permutations
        product
'''
terminal = os.get_terminal_size()
w = terminal.columns

# count -args:2 1.beginning point, 2.step(can be float). Infinite loop.
print('Count Class'.center(w, '-'))

counter = itertools.count(10)

for i in counter:
    print(i)
    
    if i == 20:
        break



# cycle -takes a sequence and creates infinite loop with it. Needs break point.
print('Cycle Class'.center(w, '-'))

l = ['A', 'B', 'C']
cycler = itertools.cycle(l) # infinite loop on l list

for i, letter in enumerate(cycler):
    print(i, letter, sep=': ')
    
    if i == 20: # break point
        break



# repeat -args:2 1.sequence, 2.repeat time(int)
print('Repeat Class'.center(w, '-'))

string = '@alicemkyn'
repeater = itertools.repeat(string, 10)
# print(list(repeater))

for string in repeater:
    print(string)



# accumulate - Fibonacci sequence (default addition)
print('Accumulate Class'.center(w, '-'))

numbers = [1, 2, 3, 4, 5]
accumulation = itertools.accumulate(numbers)
print(list(accumulation)) # [1, 3, 6, 10, 15]

#! However, we can change the default addition operation
import operator
accumulation_multiply = itertools.accumulate(numbers, operator.mul)
print(list(accumulation_multiply)) # [1, 2, 6, 24, 120]



# chain -combines the lists together as one.
print('Chain Class'.center(w, '-'))

a = [1, 2, 3]
b = ['a', 'b', 'c']
combined = itertools.chain(a, b) # or itertools.chain(a,b,a,a,b,a,b,b)
print(list(combined))



# compress -according the bool selectors generates new list
print('Compress Class'.center(w, '-'))

l = ['a', 'b', 'c', 'd']
selectors = [0, 1, 1]

compressed = itertools.compress(l, selectors)
print(list(compressed)) # ['b', 'c']



# dropwhile -args2 1.lamda, 2.sequence : drops one time then continues.
# as soon as it evaluates True drops.
print('Dropwhile Class'.center(w, '-'))

l = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3]
remaining = itertools.dropwhile(lambda n : n < 3, l)
print(list(remaining)) # [3, 4, 5, 6, 7, 1, 2, 3]



# filterfalse -args2 1.lamda, 2.sequence : filters seq. according to lambda
print('Filterfalse Class'.center(w, '-'))

l = range(100)
filtered = itertools.filterfalse(lambda n : n % 10, l)
print(list(filtered)) # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]



# groupby
print('Groupby Class'.center(w, '-'))

l = [('a', 1), ('a', 2), ('b', 3), ('b', 4), ('b', 5), ('c', 6)]
groupped = itertools.groupby(l, lambda k : k[0])

for key, values in groupped:
    print(key, list(values), sep=': ')
    
#! OR
l = [1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 2, 2]
groupped = [list(g) for k, g in itertools.groupby(l)]
print(groupped) # [[1], [2, 2, 2, 2], [3, 3, 3, 3, 3], [2, 2]]



# islice -similar to [::]
print('Islice Class'.center(w, '-'))

l = ['a', 'b', 'c', 'd', 'e', 'f']
sliced = itertools.islice(l, 2) # till index no 2
sliced2 = itertools.islice(l, 2, None) # from 2 till end

print(list(sliced)) # ['a', 'b']
print(list(sliced2)) # ['c', 'd', 'e', 'f']



# pairwise 
print('Pairwise Class'.center(w, '-'))

l = 'abcde'
paired = itertools.pairwise(l)
print(list(paired)) # [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e')]



# starmap
from operator import pow
print('Starmap Class'.center(w, '-'))

l = [(2, 3), (2, 4), (2, 5)]
star_mapped = itertools.starmap(pow, l)
print(list(star_mapped)) # [8, 16, 32]



# takewhile -opposite of dropwhile class as soon as it evaluates False, stops.
print('Takewhile Class'.center(w, '-'))

l = [1, 2, 3, 4, 5, 6, 1]
taken = itertools.takewhile(lambda a : a < 4, l)
print(list(taken)) # [1, 2, 3]



# tee - returns n times independent iterables from single iterable
print('Tee Class'.center(w, '-'))

l = [1, 2, 3, 'a', 'b', 'c']
tee = itertools.tee(l, 3)

for it in tee:
    print(list(it))
    


#! ziplongest -Most used method. fillvalue=None by default
print('Ziplongest Class'.center(w, '-'))

a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c']
c = [True, False]
# Comparison built-in zip() vs zip_longest()
zip_built_in = zip(a, b, c)
print(list(zip_built_in))

zipped = itertools.zip_longest(a, b, c)
print(list(zipped))



####################### COMBINATORIC ITERATORS #########################
#! product To Get Cartesian Product
print('Product Class'.center(w, '-'))

a = [1, 2, 3]
b = ['a', 'b', 'c']
output = itertools.product(a, b)

for t in list(output):
    print(t)



#! permutations 
print('Permutations Class'.center(w, '-'))

l = ['A', 'B', 'C']
permutations = itertools.permutations(l)
#print(list(permutations))

for g in list(permutations):
    print(*g , sep=' ')



#! combinations second argument is combination amount
print('Combinations Class'.center(w, '-'))

l = [0, 1, 2, 3]
combinations = itertools.combinations(l, 2)

for g in list(combinations):
    print(g)
    
# Never going to repeat a sequence in here. If we want to repeated sequence:

combinations = itertools.combinations_with_replacement(l, 3)

for g in list(combinations):
    print(g)