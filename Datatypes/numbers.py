################### INTEGER - FLOAT - COMPLEX ##########################

# INTEGERS
num = 1_000_000_000
print(num) # 1000000000
num = 1e12
print(num) # 1000000000000.0
print(f'{num:,}') # 1,000,000,000,000.0
print(f'{num:_}') # 1_000_000_000_000.0

ls = [i for i in dir(int) if not i.startswith('_')]
print(ls)
# ['as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']


# bit_length()
num = 10
print(num.bit_length()) # 4

statement = len(bin(10)[2:]) == (10).bit_length()
print(statement) # True
# ! 10.bit_length() won't work because python assumes it as a float 
# ! because of dot notation.



# FLOAT
# as_integer_ratio()
number = 4.5
print(number.as_integer_ratio()) # -> (9, 2)

# is_integer()
print((12.0).is_integer()) # True
print((12.5).is_integer()) # False

# float('inf')
print(float('inf')) # inf type:float


######################## BUILT-IN FUNCTIONS ############################
# CONVERSIONS
# bin() # ! takes decimal 0b shows that it is base2
# oct() # ! takes decimal 0o shows that it is base8
# hex() # ! takes decimal 0x shows that it is base16

print(int('fff', 16)) # hex to decimal
print(int('777', 8)) # oct to decimal
print(int('0101', 2)) # bin to decimal

# Hex to Bin ?
print(bin(int('86424ef', 16))) # 0b1000011001000010010011101111

