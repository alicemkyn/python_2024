'''
Syntax -> f = open('/path/file.ext' 'mode' encoding)
- f.write('str') or f.read() by default
- f.writelines(list) or f.readlines() returns list
- f.readline() -> Returns one line of file.Use in for loop
- f.readlines() Reads all info in list
- f.close() -> Writes the things in buffer.
- f.tell() Returns the cursor current position
- f.seek(number) Cursor goes to given no
- f.read() Returns str of all info in f.

OR
with open('/path/file.ext', 'mode', encoding) as file:
    file.write() or file.read()
    
METHODS
- f.closed -> bool
- f.readable() -> bool depends on open mode if r -> True
- f.writable() -> bool depends on open mode if w -> True
- f.truncate() eg. f.truncate(10) -> makes file 10 byte.
After first 10 bytes data, deletes other remaining.
- f.mode -> 'r' eg. returns the open mode
- f.name -> 'some.txt' eg. returns the file name
- f.encoding -> 'utf-8' eg. returns the encoding type.

FILE MODES
- 'r' = Default mode. If file exists, opens and reads everything,
if there is nothing to read it will return error.
- 'w' = Write mode. If the file exists deletes its content. If not creates
the file and writes the contents.
- 'a' = Append write mode. Doesn't delete the file if exists. And appends
(adds) the item to its content next to the last line. If doesn't exists,
it creates it.
- 'x' = Write mode. Difference from 'w' mode is if file exists this mode,
will give error instead of deleting its content. If not, file will be created.
- 'r+' = Read mode with write mode. File should be in the given path, otherwise
it will give error.
- 'w+' = Write mode with read mode. Same rules 'w' and you can write() and read()
together.
- 'a+' = Append mode with read mode. Same rules 'a'.
- 'x+' = Write mode with read mode . Same rules 'x'.
# BYTE MODE
- 'rb', 'wb', 'ab', 'xb', 'rb+', 'wb+', 'ab+', 'xb+'
Same rules b means byte data. + means read
'''
with open('contact.txt', 'w') as f:
    ls = ['Yuri:12345\n', 'Alex:54321\n', 'Anton:13579\n']
    f.writelines(ls)

# Changes at beginning
with open('contact.txt', 'r+') as file:
    data = file.read()
    file.seek(0)
    file.write('Nadya:24680\n'+ data)

# Changes at middle
with open('contact.txt', 'r+') as file:
    data = file.readlines()
    insert_no = round(len(data)/2)
    data.insert(insert_no, 'Sasha:11223\n')
    file.seek(0)
    file.writelines(data)

# Changes at bottomline
with open('contact.txt', 'a') as file:
    file.write('Vlad:77443\n')
