import sys

# # sys.exit() Stops the program immidiately No codes below worked.
# for i in range(0,10,1):
#     if i == 5:
#         sys.exit()
#     elif i > 5 :
#         sys.exit('Number is even')
#     else:
#         print(i)


# # sys.argv -> list & sys.argv[0] always [module.py] == python module.py
# def terminate():
#     print("Terminating....")
#     sys.exit()

# if len(sys.argv) < 2:
#     print('You didn\'t enter the necessary parameters')
#     terminate()
# elif len(sys.argv) > 2:
#     print('You\'ve entered too many parameters')
#     terminate()
# elif sys.argv[1] in ['-v', '-V']:
#     print('Program\'s version is 0.8')
# else:
#     message = 'The parameter {} is unknown you have entered.'
#     print(message.format(sys.argv[1]))
#     terminate()

# Now we should run the module in terminal with given parameters.
# Example : python sys_module.py > First if block
# Example : python sys_module.py -a > else block
# Example : python sys_module.py -a -b > First elif block
# Example : python sys_module.py -v or -V > Second elif block


# sys.executable -> running python's info
print(sys.executable) #/opt/homebrew/opt/python@3.10/bin/python3.10


# sys.path
print(sys.path)
[
    '/Users/alicemkoyun/Programming/Sys_Module', 
    '/opt/homebrew/Cellar/python@3.10/3.10.13_2/Frameworks/Python.framework/Versions/3.10/lib/python310.zip', 
    '/opt/homebrew/Cellar/python@3.10/3.10.13_2/Frameworks/Python.framework/Versions/3.10/lib/python3.10', 
    '/opt/homebrew/Cellar/python@3.10/3.10.13_2/Frameworks/Python.framework/Versions/3.10/lib/python3.10/lib-dynload', 
    '/opt/homebrew/lib/python3.10/site-packages'
    ]


# sys.platform
print(sys.platform) # darwin


# sys.prefix -> installation path of pythons active interpreter
print(sys.prefix) # /opt/homebrew/opt/python@3.10/Frameworks/Python.framework/Versions/3.10


# sys.ps1 >>> or sys.ps1 = '+++'  # works on in python shell
# sys.ps2 ... or sys.ps2 = '___' # works on in python shell


# sys.version
print(sys.version) # 3.10.13 (main, Aug 24 2023, 12:59:26) [Clang 15.0.0 (clang-1500.1.0.2.5)]


# sys.version_info
print(sys.version_info) # sys.version_info(major=3, minor=10, micro=13, releaselevel='final', serial=0)


# sys.stdout, sys.stderr
print(sys.stdout) # <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>

print(sys.stdout.write('Hello Cruel World!')) # Hello Cruel World!18 > 18 means len(given_str)
# write() method differentiates from print() > takes only str as an argument

for i in 'alicem':
    sys.stdout.write(i+'\n') # if only i > alicem%

outputs = open('outputs.txt', 'w')
errors = open('errors.txt', 'w')
sys.stdout = outputs
sys.stderr = errors
print('Output message')
print('Error Message', 1/0)


# sys.stdin > same as input()

# sys.getrecursionlimit()
print(sys.getrecursionlimit()) # 1000