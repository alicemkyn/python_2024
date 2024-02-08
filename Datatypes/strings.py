'''
Strings are IMMUTABLE datatype.
'''

########################### STRING METHODS #############################

# replace()
st = 'memleket'
print(st.replace('e', '')) # mmlkt
print(st.replace('e', '', 1)) # mmleket


# split(), rsplit(), splitlines()
st = 'Ankara Buyuksehir Belediyesi'
print(st.split()) # ['Ankara', 'Buyuksehir', 'Belediyesi']
print(st.split(' ', 1)) # ['Ankara', 'Buyuksehir Belediyesi']
print(st.rsplit(' ', 1)) # ['Ankara Buyuksehir', 'Belediyesi']
st = '''
Ankara
Buyuksehir
Belediyesi
'''
print(st.splitlines()) # Entera basilan yerlerden boler list dondurur.
# ['', 'Ankara', 'Buyuksehir', 'Belediyesi']
print(st.splitlines(True)) # True ile \n gosterir.
# ['\n', 'Ankara\n', 'Buyuksehir\n', 'Belediyesi\n']


# lower()
st = 'LOWER'
print(st.lower()) # lower

# upper()
st = 'upper'
print(st.upper()) # UPPER

# islower() -> Bool
# isupper() -> Bool
# startswith() -> Bool
# endswith() -> Bool

# capitalize()
st = 'capitalize'
print(st.capitalize()) # Capitalize


# title()
st = 'python programming language'
print(st.title()) # Python Programming Language


# swapcase() lowers the uppers, uppers the lowers 
st = 'python, PYTHON, Python'
print(st.swapcase()) # PYTHON, python, pYTHON


# casefold() Same like lower()


# strip(), lstrip(), rstrip()
st = 'python'
print(st.strip('p')) # ython
# strip() only look beginning and the end of the str.
st = 'kazak'
print(st.strip('k')) # aza
print(st.lstrip('k')) # azak
print(st.rstrip('k')) # kaza
# Parametresiz implementasyonu varsa bosluk, \t, \n, \r, \v, \f kirpar.


# join() 'birlestirme_karakteri'.join(liste) -> split() metodunun tersi.
st = 'Besiktas Jimnastik Kulubu'
ls = st.split() # ['Besiktas', 'Jimnastik', 'Kulubu']
st2 = ' '.join(ls) # Besiktas Jimnastik Kulubu
st3 = '.'.join(i for i in st if i.isupper()) # B.J.K


# count()
st = 'Canada'
print(st.count('a')) # 3
print(st.count('a', 1,4)) # 2 (1,4 are index st[1:4])


# index(), rindex()
st = 'Canada'
print(st.index('a')) # 1 gives the first match index
print(st.rindex('a')) # 5 right - left


# find(), rfind()
# Same as index() and rindex(). Only difference is if index() cant find
# sth, it will give error and ends the program. But find() and rfind()
# will return -1 instead if cant find the given words index.


# center() arg should be bigger than len(a)
st = 'apple'
print(st.center(11))
#    apple   
print(st.center(11, '-'))
# ---apple---


# rjust(), ljust()
st = 'apple'
print(st.ljust(10, '.')) # apple.....
print(st.rjust(10, '.')) # .....apple


# zfill()
st = '12'
print(st.zfill(3)) # 012


# partition(), rpartition() #Divides into 3 pieces(before, given, after)
st = 'istanbul'
print(st.partition('an')) # ('ist', 'an', 'bul')
print(st.partition('h')) # ('istanbul', '', '')
st = 'istihza'
print(st.rpartition('i')) # ('ist', 'i', 'hza')
print(st.rpartition('r')) # ('', '', 'istihza')


# encode()
print('çilek'.encode('utf8')) # b'\xc3\xa7ilek'

# expandtabs()
print('apple\tis\ta\tfruit.'.expandtabs(20))
# apple               is                  a                   fruit.


#str.maketrans(), translate()
text = 'Türkçe, ağır, şans, öğrenci'
src = 'şçöğüıŞÇÖÜĞI'
target = 'scoguiSCOUGI'
trnslt = str.maketrans(src, target)
print(trnslt)
#{351: 115, 231: 99, 246: 111, 287: 103, 252: 117, 305: 105, 350: 83, 199: 67, 214: 79, 220: 85, 286: 71, 73: 73}
print(text.translate(trnslt)) # Turkce, agir, sans, ogrenci

toDelete = 'şçöğüıŞÇÖÜĞI'
trnslt = str.maketrans('', '', toDelete) # Third parameter is for delete
print(text.translate(trnslt)) # Trke, ar, ans, renci

# Using all three paramaters together
text = 'Cem Yilmaz'

src = 'CY'
target = 'cy'
toDelete = 'eia '
trnslt = str.maketrans(src, target, toDelete)
print(text.translate(trnslt)) # cmylmz


# isalpha() 'abcdef...'
# isdigit() '12345...'
# isalnum() '123abc456'
# isdecimal() '123'True '123.3'False
# isidentifier() # Checks the name is definable as func, var, module.
# isnumeric() '12345...'
# isspace() Everything is space? or False.
# isprintable() 'a' -> True, '\n' -> False

