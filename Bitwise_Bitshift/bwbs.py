############################# BITWISE ##################################
'''
& And Operator
| Or Operator
^ Xor Operator
'''
print(int('1111', 2)) # 15
print(int('1100', 2)) # 12
print(int('1010', 2)) # 10
print(int('0101', 2)) # 5

# AND
print(15 & 0) # 1111 & 0000 > 0000 > 0
print(12 & 10) # 1100 & 1010 > 1000 > 8
print(5 & 10) # 0101 & 1010 > 0000 > 0

# OR
print(15 | 0) # 1111 | 0000 > 1111 > 15
print(12 | 10) # 1100 | 1010 > 1110 > 14
print(5 | 10) # 0101 | 1010 > 1111 > 15

#XOR
# If the operands are different then 1 otherwise they are same 0
print(5 ^ 3) # 0101 ^ 0011 > 0110 > 6



############################# BITSHIFT #################################
'''
<<< Left Shift = Add Zero to Least Significant Bits and *2
>>> Right Shift = Add Zero to Most Significant Bits and /2
'''

# RIGHT SHIFT /2
# 1100 > 12 if we right shift it 1 time it loses its last bit and 0 comes to first bit
print(12 >> 1 ) # 6 > 0110
print(12 >> 2) # 3 > 0011

# LEFT SHIFT *2
# 1011 > 11 if we left shift it 1 time 0 added to last bit
print(11 << 1) # 22 > 10110
print(11 << 2) # 44 > 101100
