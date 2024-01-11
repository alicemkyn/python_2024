import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''
########################################################################

text_to_search = """
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
.[{()\^$|?*+

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234


Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat

"""
########################################################################

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
########################################################################

sentence = "Start a sentence and then bring it to the end"

# r means raw string. e.g > r'some string'
# to eschew any mistakes better to use regex on raw strings.

pattern = re.compile(r'abc') # span(1,4) match='abc'
pattern1 = re.compile(r'cba') # None
pattern2 = re.compile(r'.') # everything except new line
pattern3 = re.compile(r'\.') # all the dots in the text
pattern4 = re.compile(r'coreyms\.com') # coreyms.com
pattern5 = re.compile(r'\d') # only all digits
pattern6 = re.compile(r'\D') # Capital negates the previous > NOT Digits
pattern7 = re.compile(r'\w') # most common one (see snippets.txt)
pattern8 = re.compile(r'\W') # white sp. metachr. newlines
pattern9 = re.compile(r'\s') # space,tab,newline
pattern10 = re.compile(r'\bHa') # Ha Ha not the last Ha 
pattern11 = re.compile(r'\BHa') # Ha only the last one which has no boundary.
pattern12 = re.compile(r'^Start') 
pattern13 = re.compile(r'end$') 

# To find the phone numbers
pattern14 = re.compile(r'\d\d\d\.\d\d\d\.\d\d\d\d') #123.555.1234 
pattern15 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # 321-555-4321
pattern16 = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') # Both number
pattern17 = re.compile(r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d') # Both number
pattern18 = re.compile(r'[89]00[.-]\d\d\d[.-]\d\d\d\d') # 800 and 900 only

# Negating with ^ inside character set
pattern19 = re.compile(r'[^b]at') # cat mat pat NOT bat

#Quantifiers
pattern20 = re.compile(r'\d{3}.\d{3}.\d{4}') # all phone numbers
pattern21 = re.compile(r'Mr\.?\s[A-Z]\w*') # before ? means it is optional

#Groups
pattern22 = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')

# Lets try to write regex for emails
pattern23 = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.com')
pattern24 = re.compile(r'[a-zA-Z.]+@[a-zA-Z]+\.(com|edu)')
pattern25 = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
pattern26 = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

# Lets try for urls
pattern27 = re.compile(r'https?://(www\.)?\w+\.\w+') # regex for all urls
pattern28 = re.compile(r'https?://(www\.)?(\w+)(\.\w+)') # groupped
# group0 everythin group1 www group2 domain name group3 top level domain
subbed_urls = pattern28.sub(r'\2\3',urls) # 2 and 3 are group numbers
print(subbed_urls) # domainname.topleveldomain

# Flags
pattern29 = re.compile(r'start',re.IGNORECASE) # or re.I
match = pattern29.search(sentence)
print(match) # Start

matches = pattern22.finditer(text_to_search)
matches = pattern26.finditer(emails)
matches = pattern28.finditer(urls)
#matches = pattern12.finditer(sentence)
#matches = pattern13.finditer(sentence)

for match in matches:
    print(match)

for match in matches:
    print(match.group(0)) # all urls
    print(match.group(1)) # www
    print(match.group(2)) # domain name
    print(match.group(3)) # top level domain
    
#print(text_to_search[1:4]) # abc span(1,4)


# To find email adresses from the data.txt file
with open('data.txt', 'r', encoding='utf8') as f:
    contents = f.read()
    pattern_phone = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    pattern_p1 = re.compile(r'[a-zA-Z1-5]')
    pattern_p2 = re.compile(r'[^a-zA-Z]') # Negates
    matches = pattern_p2.finditer(contents)
    
    #for match in matches:
       # print(match)


with open('data.txt', 'r', encoding='utf8') as f:
    rd = f.read()
    pttrn = re.compile(r'(\w+)@(.+\..{3})',re.I)
    print(pttrn.sub(r'\1@alicem.com',rd))
    _, number = pttrn.subn(r'\1@alicem.com',rd)
    print(number,'times changed')
    with open('data_changed.txt','w', encoding='utf8') as y:
        y.write(pttrn.sub(r'\1@alicem.com',rd)+f'\n{number} times changed')
        
    