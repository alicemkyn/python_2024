# Escape Sequence 
**\a\t\b\u\n\U\N \r\v r\b \f\x**
### \n
New Line
### \
Deactivate Right \\', \\",  \\\ 
### \t
TAB, Indentation Horizontal
### \a
Alarm
### \r
Carriage Return (Overwrite From Beginning)
### \v
Vertical TAB
### \b
Slaughter or back. Cursor one step left.
### \u 
Unicode Codepoint 4 digit - \u0131
### \U 
Unicode Codepoint 8 digit - \U00000131
### \N 
Unicode Long Name - print('\N{LATIN SMALL LETTER A}')
### \x
Unicode Hex Code Point - '\x4E' == 'N'
### r
Raw string or Deactivates everything inside the str.
### \f
Newpage f = open('text.txt', 'w'); print('deneme\fdeneme', file=f)
