########################## GENERATORS ##################################
'''
*** Generator are iterables ! Best thing about generators is we can use
them with for loops.

* In nested functions 'local' values were being deleted and 'nonlocal'
values were staying. But in generators nothing is deleted neither variables
are removed, nor other values are set 0.

* After return no code line will work but after yield code flows and works.
yield is the indication of generators and it doesnt end the function
like return.

* If the topic is generators then we should know about two built-in 
functions. iter() and next().
-iter() works only if there is a loop inside.
-next() opposite of iter() if there is no loop inside we use next()

* If a generator is defined in while True loop and trying to yield the values
in for loop it will stuck in infinite loop. To prevent this we should use
if statement to check the determined value and keep it under control and 
end the generator with return. If there is nothing written next to return
it will return None and end the generator.

* After defined type(gen)= class 'function'. But when we call it now it 
becomes and generator object. a = gen(); type(a) -> class 'generator'
'''

# Fibonacci Example

def fibonacci(): 
    x=1
    y=0
    z=0
    while True:
        z=y 
        y=x 
        x=y+z 
        yield x
# Above it is a class 'function'.

f= fibonacci() # Now it is a generator object
print(next(f)) # 1
print(next(f)) # 2
print(next(f)) # 3
print(next(f)) # 5
print(next(f)) # 8
print(next(f)) # 13
print(next(f)) # 21
print(next(f)) # 34

# Infinite loop 
#for i in fibonacci():
    #print(i)

def fibonacci(): 
    x=1
    y=0
    z=0
    while True:
        z=y 
        y=x 
        x=y+z 
        yield x
        if x > 100:
            return # To break the loop or use 'break'

for i in fibonacci():
    print(i) # 144


# Another example with generators under the for loop
def generator(num):
    for i in range(num):
        print("Hello")
        yield 'World'

for i in generator(4):
    print(i)

# Another approach to the same generator
y = generator(5) # it is now a generator object
a = iter(y) # We have loop inside.

print(next(a), 'From another approach')
print(next(a), 'From another approach')
print(next(a), 'From another approach')
print(next(a), 'From another approach')
print(next(a), 'From another approach')
# print(next(a), 'From another approach')
# Last print raises StopIteration error and ends the loop.

# OR
for i in y:
    print(next(a))
    

######################## Yield From Statement ##########################
'''
Yields the values from another generator object.
'''
def generator1():
    yield "generator1 started."
    yield 'generator1 ended.'
    
def generator2():
    yield 'generator2 started.'
    yield from generator1()
    yield 'generator2 ended.'
    
for i in generator2():
    print(i)
'''
generator2 started.
generator1 started.
generator1 ended.
generator2 ended.
'''