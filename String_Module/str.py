import string
'''
Formatter : <class 'string.Formatter'>
Template : <class 'string.Template'>
ascii_letters : abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
ascii_lowercase : abcdefghijklmnopqrstuvwxyz
ascii_uppercase : ABCDEFGHIJKLMNOPQRSTUVWXYZ
capwords : <function capwords at 0x1007179a0>
digits : 0123456789
hexdigits : 0123456789abcdefABCDEF
octdigits : 01234567
printable : 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 



punctuation : !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
whitespace :  



'''

#print(help(string))

ls = [i for i in dir(string) if not i.startswith('_')]
print(string.__all__)
for i in ls:
    attribute_val = getattr(string, i)
    print(f'{i} : {attribute_val}')