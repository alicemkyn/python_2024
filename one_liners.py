############################# ONE LINERS ###############################

# Print System's Hostname
from socket import gethostname; print(gethostname()) #Alicems-MacBook-Pro.local

# Read Lines From a File
lines = [l.strip() for l in open('word_file.txt')]

# Count lines In a File
line_count = sum(1 for line in open('word_file.txt'))

# Extract Digits From a String
my_string = "41I C3M K0YUN"
digits = ''.join(filter(str.isdigit, my_string))
print(digits) # '4130'

# Remove Dups From List
original_list = ['ali', 'cem', '4', '444', 'cem', '444', '4' ] * 2
print(original_list)
unique_list = list(set(original_list))
print(unique_list) # ['cem', '4', 'ali', '444']

# Calculate Average of List
my_list = [*range(10)]
average = sum(my_list) / len(my_list) if len(my_list) > 0 else 0
print(average) # 4.5

# Generate a Fibonacci Sequence 
fibonacci = lambda n : n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10))

# Conditional Value Assignment
x = 10
y = '100'
result = y if isinstance(y, int) and y % 2 == 0 else x
print(result)

# Handle Zero Divison Error
numerator, denominator = 2, 0
result = numerator / denominator if denominator != 0 else 0
print(result)

# One Liner try - except Block
try_block = lambda : True
except_block = lambda : False
result = try_block() if 2/2 == 2 else except_block()
print(result)

# Fetch HTML Content With requests
import requests; html_content = print(requests.get('https://httpbin.org').text)

# Generating a list of leap years using list comprehension
lp_yr = [year for year in range(2000,2051) if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]
print(lp_yr)

# Retrieve Public IP Adress
public_ip = requests.get('https://api64.ipify.org?format=json').json()['ip']
print(public_ip)

# Hashing with hashlib
import hashlib
hashed_password = hashlib.sha256('12345alicem'.encode()).hexdigest()
print(hashed_password)

# sorted to Find largest number in a list or str
longest = sorted(['alicem','koyun'], key=len)
second_largest = sorted([3,4,11,345,43,123,131])[-2]
print(longest, second_largest)

# Check if a number is prime
is_prime = all(7 % i != 0 for i in range(2,7) )
print(is_prime)

# Find the most common element in a list
most_common = max(set([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]), key=[1, 2, 2, 3, 3, 3, 4, 4, 4, 4].count)
print(most_common) # 4

# Find the most common word in a list
words = ['alicem','ali', 'cem ','cem','cem', 'ali', 'ali']
most_common_word = max(words, key=words.count)
print(most_common_word) # 'ali'

# Merge two dictionaries
dict_1 = {'name' : 'Alicem', 'age':29}
dict_2 = {'name' : 'Alicem', 'surname':'Koyun', 'age':29}
merged_dict = {**dict_2, **dict_1}
print(merged_dict) # {'name': 'Alicem', 'surname': 'Koyun', 'age': 29}

# Find the first occurrence of an item in a list:
my_list = [*range(10)]
index = next((i for i, v in enumerate(my_list) if v == 9), None)
print(index) # 9

# Remove vowels from a string
my_string = 'Alicem Koyun'
without_vowels = my_string[0] + ''.join(char for char in my_string[1:] if char.lower() not in 'aeiou')
print(without_vowels) # Alcm Kyn

# Removing duplicates from a list while preserving order
unique_list = list(dict.fromkeys([1,2,2,3,3,4,4,4]))
print(unique_list) # [1, 2, 3, 4]

# Removing white spaces from beginning and end of a string
trimmed_str = '  hello world  '.strip()
print(trimmed_str) # hello world

# Parsing and extracting information from a string using regular expression
import re 
extracted_digits = re.findall(r'\d+', 'abc123def456')
print(extracted_digits) # ['123', '456']

# Swapping case in a string using a list comprehension
swapped_case = [''.join(char.upper() if char.islower() else char.lower() for char in "Hello World!")]
print(swapped_case) # ['hELLO wORLD!']

# Converting a binary string to an integer
binary_to_int = int('1101', 2)
print(binary_to_int)

# Filtering out non-positive numbers from a list
positive_numbers = list(filter(lambda x: x > 0, [-2,-3,0,3,-1,5,4]))
print(positive_numbers) # [3, 5, 4]

# Extract all email adresses from text:
emails = re.findall(r'\b[\w.+-]+@[\w-]+\.[\w.-]+\b','alicemkoyun@gmail.com')

# Validate a phone number format
pattern = re.compile(r"^\+?[\d\s]{7,}$")
phone = pattern.match('+905323131')

# Download a file from URL
from urllib.request import urlretrieve
urlretrieve("https://httpbin.org/anything", 'downloaded_file.zip')

# Check website status efficiently
response = requests.get('https://httpbin.org/anything').status_code
print(response) # 200

# List files in directory
import os
files = [f for f in os.listdir('./') if os.path.isfile(os.path.join('./', f))]
print(files) # ['application.db', 'word_file.txt', '.DS_Store', 'downloaded_file.zip', 'test.py', '.gitignore']

# Get system information like CPU usage
import psutil
print(os.cpu_count(), psutil.cpu_percent())

# To usage of dir and see the methods of datatypes or builtin functions
assertion = 'sort' in dir(list) and 'sorted' in dir(__builtins__)
print(assertion) # True