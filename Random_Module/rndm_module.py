import random
'''
random is actually not random. It has a deterministic approach,
so taken a value from hour or microsecond of OS than makes modular arithmetics to create random digits.
To see more try random.seed(10) and every random int results 
will be the same.
Before python 3.2 people would use random.seed = os.urandom(1024) to make it more reliable, unpredictable, and secure.
urandom is a OS file and random byte value is determined by system itself.
'''
# 1- random() # Gives random float between 0 and 1
print(random.random()) # 0.583588501991895

# 2- uniform() # Same with random but we can give args and set interval.
print(random.uniform(1,5)) # 4.485783255682247
print(random.uniform(0.5, 0.9)) # 0.5633287278321941

# 3- randint() # This returns random int value within the given interval.
print(random.randint(4, 44)) # 13

# 4- choice() # We can select random values in iterables.
ls = ['ali', 44,'cem', 'koyun', 4, 'ankara', 'vancouver', True, None]
print(random.choice(ls)) # vancouver
strng = 'Alicem Koyun'
print(random.choice(strng)) # e

# 5- shuffle() # We can shuffle the mutable datatypes b'cuz this method is inplace.
ls = [*range(10)]
print(ls) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(ls) # Inplace action called
print(ls) # [3, 9, 1, 8, 6, 2, 4, 7, 0, 5]

# 6- randrange() # Same with randint() returns one int 
print(random.randrange(5)) # 3
print(random.randrange(10,13)) #10 #13 

# 7- sample() # takes iterable first and piece of sample as second args.
l = ['ali', 44,'cem', 'koyun', 4, 'ankara', 'vancouver', True, None]
# Lets say that we want to collect 4 random samples from this list.
print(random.sample(l, 4)) # ['vancouver', True, 'cem', 4]

# 8 random.seed() # Determine the seed manually to get same results everytime.
random.seed(10)
print(random.random()) # 0.5714025946899135
random.seed(10)
print(random.random()) # 0.5714025946899135
