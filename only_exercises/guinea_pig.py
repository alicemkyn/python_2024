# # Problem1
# for i in range(1000):
#     total = 0
#     for j in range(1,i):
#         if i % j == 0:
#             total += j
#     if total == i:
#         print(i)


# for i in range(1,1001):
#     total = 0
#     for j in range(1,i):
#         if i % j == 0:
#             total += j
#     if total == i:
#         print(i ,"is perfect")

# # Problem 2
# for i in range(1,10000):
#     chcker = 0
#     remainder = 0
#     b = str(i)
#     b = len(b) # exponent value
#     real_i = int(i)
#     while i > 0 :
#         remainder = i % 10
#         chcker += remainder ** b
#         i //= 10
#     if chcker == real_i:
#         print (real_i)


# for i in range(1,10000):
#     b = str(i)
#     total = 0
#     reali = i
#     while i > 0:
#         total += (i % 10) ** len(b)
#         i //= 10
#     if total == reali:
#         print (reali,"armstrong")


# # Problem 3
# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i} x {j} = {i*j}")

# for i in range(1,11):
#     for j in range (1,11):
#         print(f"{i} x {j} = {i*j}")


# Problem 4

# total = 0
# while True:
#     a = input("sayi girin:  yada cikin q veya Q")
#     if a == "q" or a == "Q":
#         print(total)
#         break
#     else:
#         b = int(a)
#         total += b


# total = 0
# while True:
#     a =input("sayi girin: cikmak icin q ya basin")
#     if a == "q" or a=="Q":
#         print(total)
#         break
#     else:
#         total += int(a)


# # Problem 5
# for i in range (1,1001):
#     if i % 2 == 0:
#         continue
#     else:
#         print(i)


# for i in range(1,101):
#     if i % 2 == 0:
#         continue
#     else:
#         print(i)


# Problem 6
# listt = [i for i in range(1001) if i % 2 ==0]
# print(listt)

# listt = [i for i in range(1,101) if i % 2 == 0]
# print(listt)


# # Problem 7
# list = [1,3,4,5,6,7,8,12,54,23,11,75,22,9]
# lsttek = []
# lstcift =[]
# for i in list:
#     if i % 2 == 0:
#         lstcift.append(i)
#     else:
#         lsttek.append(i)
# lsttek.sort(), lstcift.sort()
# print(lsttek,lstcift)


# list = [1,3,4,5,6,7,8,12,54,23,11,75,22,9]
# listtek = [i for i in list if i % 2 == 0]
# listcift =[i for i in list if i % 2 != 0]
# listtek.sort(),listcift.sort()
# print(listtek,listcift)


# Problem 8

# for i in range(1,101):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#         else:
#             print(i)
#             break


# for i in range(1,101):
#     for j in range(2,(i+1)):
#         if i % j == 0:
#             if i != j:
#                 break
#             if i == j:
#                 print(i)
#                 break

# Problem 9
# total = 1
# for i in range(1,101):
#     total *= i
# print(total)

# total = 1
# for i in range(1,101):
#     total *= i
# print(total)


# Problem 10

# a = 1
# b = 1
# liste = [a,b]
# for i in range(1,101):
#     a , b = b , b + a
#     liste.append(b)
# print(liste)


# Problem 13
# s = "A man , a plan , a canal: Panama"
# s1 = "".join (i for i in s if i.isalnum())
# s1 = s1.lower()
# print(s1)
# if s1 == s1[::-1]:
#     print("palindrome")
# else:
#     print("not PAlindrome")


# Problem 14

# list = [1,3,4,5,6,7,8,12,54,23,11,75,22,9]
# for i in list:
#     if i in list:
#         print(list.index(i))

# list = [1,3,4,5,6,7,8,12,54,23,11,75,22,9]
# while True:
#     a = int(input("sayi girin:"))
#     if a in list:
#         print(f"Evet var {list.index(a)} inci indeksinde")
#     else:
#         print("yok")

# Problem 15
# for i in range(1,10):
#     print(f"{i}"*i)

# Problem 16
# for i in range(1,10):
#     print("ONGUN"*i)

# Problem 18
# while True:
#     a = int(input("sayi a "))
#     b = int(input("sayi b"))
#     c = int(input("sayi c"))
#     liste = []
#     liste.append((a,b,c)) # append tek arguman alabilir o yuzden cift parantez alarak a,b,c yi tek bir tuple olarak ekler.
#     liste.extend(a,b,c) #extend ise multi arguman alir ve ikinci parantezlere gerek kalmaz.o yuzden appendeki 3 lu tek bir tuple argumani olusturdugu icin 3 u tek iterable olur ama extende 3 ayri iterable olusur.
#     liste.sort()
#     print(liste[-1])


# while True:
#     c =int (input("deger girin"))
#     b =int (input("deger girin"))
#     a=int (input("deger girin"))
#     list=[]
#     list.extend((a,b,c))
#     list.sort()
#     print(list[-1])


# listeee = []
# while True:
#     a = input("sayi girin:   veya cikmak ve en buyuk girdiginiz sayiyi gormek icin q ya basin")

#     if a == "q" or a == "Q":
#         listeee.sort()
#         print(listeee[-1])
#         break
#     else:
#         listeee.append(a)


# Problem 28
# def perfect():
#     for i in range(1,1000):
#         total = 0
#         for j in range(1,i):
#             if i % j == 0:
#                 total += j
#         if total == i:
#             print(i)

# perfect()


# def perfect(sayi):
#     tot = 0
#     for i in range(1,sayi):
#         if sayi % i == 0:
#             tot += i
#     return tot == sayi

# for i in range(1,1001):
#     if perfect(i):
#         print(i)

# def even(number):
#     if not(number % 2):
#         return number

# lst = [even(i) for i in range(1,100) if even(i) and i>20]
# print(lst[:])

# liste = [*range(1,10001)]
# while len(liste) > 1:
#     j = liste[-1] #eger listenin son elemani listeden atilmiyorsa dongu basa dondugunde ilk eleman atilmalidir
#     for i in liste[1::2]:
#         liste.remove(i)
#     if j in liste:
#         liste.pop(0)
# print(liste)


# Problem 39 Luhn's Algorithm
# Python3 program to implement
# Luhn algorithm

# Returns true if given card
# number is valid

# From internet we got the code to try Luhn's algorithm ####Decomment the lines below from here:####

# def checkLuhn(cardNo):

#     nDigits = len(cardNo)
#     nSum = 0
#     isSecond = False

#     for i in range(nDigits - 1, -1, -1):
#         d = ord(cardNo[i]) - ord('0')

#         if (isSecond == True):
#             d = d * 2

#         # We add two digits to handle
#         # cases that make two digits after
#         # doubling
#         nSum += d // 10
#         nSum += d % 10

#         isSecond = not isSecond

#     if (nSum % 10 == 0):
#         return True
#     else:
#         return False

# # Driver code
# if __name__=="__main__":

#     cardNo = "4583188157394473"

#     if (checkLuhn(cardNo)):
#         print("This is a valid card")
#     else:
#         print("This is not a valid card")


# determining multi intervals with angular brackets never did it before....
# a = int(3)

# if 0 < a <4:
#     print("well done")
# else:
#     raise ValueError

# Generator CC no
# def cclencheck(ccno):
#     try:

#     strccno = str(ccno)
#     if len(ccno) == 16:


###### CC VALIDITY CHECKER ########
# https://www.youtube.com/watch?v=PNXXqzU4YnM&t=184s  check it out for Luhn's Algorithm
# https://www.validcreditcardnumber.com/ check here.
# IIN numbers to create perfection about credit card generation.To see how, check this out (below)
# https://www.investopedia.com/terms/i/issuer-identification-number-iin.asp#:~:text=The%20issuer%20identification%20number%20%28IIN%29%20refers%20to%20the,to%20the%20issuer%20and%20its%20partnering%20network%20provider.?msclkid=3f4ce2d4c27911ec838b57111e97c196

# Weight pattern is 2-1-2-1-2-1-2-1...
# Should be 16 digits
# [::2]*2 and [1::2]*1 if result > 10 while multiplication then twodigit % 10 and twodigit//10 sum the results
# if multiplication result > 10 then twodigit % 10 and twodigit//10 sum the results
# Sum of the last generated 16 digit list should be divisible by ten. So last digit of sum should be zero
# Randomly create number in interval of IIN checking method


# Function list
# ccnumber lenght check if it is 16 or not
# Weight pattern calculator and making list put of it
# Sum of the list calculator and mod 10 checker
# IIN checker:
# American Express: 34, 37
# Discover Card: 6011, 622126 to 622925, 624000 to 626999, 628200 to 628899, 64, 65
# Mastercard: 2221 to 2720, 51 to 55
# Visa: 4
# Randomly create number in interval of IIN checking method .randint


##### Generator ######
# def randomIIN():#Issuer Identification Number
#     """This function generates 16 digit numbers within specificly
#     determined intervals.

#     Returns:
#         randomint : no args
#     """
#     import random
#     randval0 = random.randint(3400000000000000,3499999999999999)
#     randval1 = random.randint(3700000000000000,3799999999999999)
#     randval2 = random.randint(4000000000000000,4999999999999999)
#     randval3 = random.randint(5100000000000000,5199999999999999)
#     randval4 = random.randint(6011000000000000,6011999999999999)
#     return randval0, randval1, randval2, randval3, randval4

# def chklen(*digits):
#     """This function checks if cc number lenght is 16

#     Returns:
#         returns tuple: takes * argument to unpack the tuple
#     """
#     verified_digits = tuple()
#     for i in digits:
#         if len(str(i)) == 16:
#             verified_digits += (i,)
#     else:
#         pass
#     return verified_digits

# def w_pattern(*digits):
#     """This function adds values and mutates them through specific
#     weight pattern
#     mutable digits = * args
#     """
#     dgt_str = [str(x) for x in digits]

#     verified_list = []
#     needed_list = []

#     for i in dgt_str:
#         newlist = []
#         result = 0
#         k = 1
#         for h in i[::2]:
#             a = int(h) * 2
#             if a < 10:
#                 newlist.append(a)
#             else:
#                 a = (a % 10) + (a // 10)
#                 newlist.append(a)
#             for j in i[k:k+1]:
#                     newlist.append(int(j))
#                     k += 2
#         for m in newlist:
#             result += m
#         if (result % 10) == 0:
#             newlist = "".join(str(x) for x in newlist)
#             if len(newlist) == 16:
#                 verified_list ="".join(str(z) for z in newlist)
#                 needed_list.append(i)
#         else:
#             continue
#     if not needed_list:
#         pass
#     else:
#         for i in needed_list:
#             if i[0:2] == "34" or i[:2] == "37":
#                 return i,"is American Express"
#             elif i[0] == "4":
#                 return i,"is Visa"
#             elif i[:2] == "51":
#                 return i,"is Mastercard"
#             else:
#                 return i,"is Discover card"


# for i in range(1,101):
#     print(w_pattern(*chklen(*randomIIN())))


# list = [1,2,6,12,234,"123","12344","osman","helloworld123",(123,3333,11123)]
# def lstto_str(list):
#     ttl = 0
#     for i in list:
#         str(i)
#         for j in str(i):
#             try:
#                 ttl += int(j)
#             except:
#                 pass
#     return ttl
# print(lstto_str(list))


###### TRIN(Turkish Republic Identification Number) Generator ########
# Should be 11 digits(first 9 digit is original digit + 2 last digit is checksum)
# 0 cant be the x[0]
# random.randint 9 digit number > convert to str > iterate for int
# ((sum of 1,3,5,7,9 digits )* 7) - (sum of 2,4,6,8 digits) % 10 = 10th digit- i in x[::2] -- i in x[1::2]
# Sum of every digit 1...+10= % 10 is 11th digit
# Ataturk's tcn= 100000001+cheksum digits

# def rnd_generate():#Generates 9 digit random number
#     """random 9 digit number generator

#     Returns:
#         int: 9 digit random number
#     """
#     import random
#     a = random.randint(100000000,999999999)
#     return a

# def w_pattern(digit):#Algorithmic Weight Pattern
#     total= 0
#     total1 = 0
#     tenth = int()
#     eleventh = int()
#     a = str(digit)
#     liste = [digit]
#     for i in a[::2]:
#         total += int(i)
#     total *= 7
#     for j in a[1::2]:
#         total1 += int(j)
#     tenth = (total - total1) % 10
#     liste.append(tenth)
#     total = 0
#     for i in liste:
#         for j in str(i):
#             total += int(j)

#     eleventh = total % 10
#     liste.append(eleventh)
#     a = "".join(str(x) for x in liste )
#     return a

# print(w_pattern(rnd_generate()))

######################################################################################################

# To find next or previous one = without cheksum digits -29999 or + 29999
# This program returns 20 tckn once it is executed.
# This one has same algotrithm as above but this is not a function.

# l = 20 # Returnsk 20 values
# digit = 333852669 # mine number raw (without last 2 digits(checksum digits))
# while l > 1:
#     digit += 29999 # everytime it turns it finds the next person after me
#     total= 0
#     total1 = 0
#     tenth = int()
#     eleventh = int()
#     a = str(digit)
#     liste = [digit]
#     for i in a[::2]:
#         total += int(i)
#     total *= 7
#     for j in a[1::2]:
#         total1 += int(j)
#     tenth = (total - total1) % 10
#     liste.append(tenth)
#     total = 0
#     for i in liste:
#         for j in str(i):
#             total += int(j)
#     eleventh = total % 10
#     liste.append(eleventh)
#     a = "".join(str(x) for x in liste )
#     print(a)
#     l -=  1

# #Fibonacci
# a= 1
# b = 1
# liste = []
# liste.extend((a,b))
# for i in range(101):
#     a,b = b,b+a
#     liste.append(b)
# print(liste)


# 2D ARRAY
# new_lst =[]
# lst = [[1,2,3],[4,5],[6]]
# for i in lst:
#     for j in i:
#         new_lst.append(j)
# print(new_lst)


# Problem 44
# Remove the duplicates and print as list
# lst = [1,1,2,3,3,3,4,5,5]


# 1 WAY FOR LOOP
# newlst = []
# lst = [1,1,2,3,3,3,4,5,5]
# for i in lst:
#     if i not in newlst:
#         newlst.append(i)
#     else:
#         continue
# print(newlst)


# 2 WAY LIST TO SET AND VICE VERSA
# lst = [1,1,2,3,3,3,4,5,5]
# sett = set(lst)
# print(sett)
# lst = list(sett)
# print(lst)

# 3 WAY
# lst = [1,1,2,3,3,3,4,5,5]
# sett = {x for x in lst}
# print(sett)
# lst = [x for x in sett]
# print(lst)


# lst = [1,1,2,3,3,3,4,5,5]
# for i in range(len(lst)):
#     for j in range(len(lst)):
#         for k in range(len(lst)):
#             if j != i != k:
#                 if i + j + k == 13:
#                     print(i,j,k)
#                     break


# lst = [1,2,3,4,5]

# multiplyArray = 1
# for i in lst:
#     multiplyArray *= i
# print(multiplyArray)

# for i in lst:
#     for j in lst:
#         if i != j:
#             if i * j == 20:
#                 print(i,j)

# def multiplyArray(numbers):
#     total = 1
#     for i in numbers:
#         for j in numbers:
#             if i * j == 20:
#                 return i ,j

# print(multiplyArray(lst))


# srt = "111101000101010101110001010000"
# print(srt.count("0"))


# liste = []
# for i in srt:
#     if i == "0":
#         liste.append(i)
# print(len(liste))

# for i in range(1,101):
#     for j in range(1,101):
#         c = ((i**2) + (j**2)) ** 0.5
#         if c == int(c):
#             print((i,j,int(c)))

# def pisagor():
#     a = tuple()
#     for i in range(1,101):
#         for j in range(1,101):
#             c = ((i ** 2) + (j **2))** 0.5
#             if c == int(c):
#                 a += (i,j,int(c)),
#     return a

# print(pisagor())

# a = int(input("sayi girin"))
# b = []
# listt= ["","bir","iki","uc","dort","bes","alti","yedi","sekiz","dokuz"]
# for i in str(a):
#     b += listt[int(i)]
# print(b)

# def prime(number):
#     lst_prm = []
#     for i in range(2,number):
#         for j in range(2,i+1):
#             if i % j == 0:
#                 if i == j:
#                     lst_prm.append(i)
#             break
#     return lst_prm

# for i in range(2,101):
#     print(prime(i))


# explanation: "amanaplanacanalpanama"
# output: True
# s1 = 121
# s = "A man , a plan , a canal: Panama"
# def palindrome(s):
#     if s != str(s):
#         s = str(s)
#     sss1 ="".join(i for i in s if i.isalnum())
#     sss1 = sss1.lower()
#     if sss1 == sss1[::-1]:
#         return True,sss1
#     else:
#         return False
# print(palindrome(s))

# def toplama(*sayi):
#     top = 0
#     for i in sayi:
#         top += i
#     print(top)
# toplama(1,2,3,4,5,5)


# s= "heyho lets go!"
# print(s[0])
# print(s[1])
# print(s[1:])

# file= open("E:/Udemy Python/ALLCODINGexercises/Next Level Modules/imdb_req_soup_udemy.py","w")
# file = open("E:/Udemy Python/ALLCODINGexercises/Next Level Modules/requests_json_doviz_app_ud.py","w")

# def lovefunc(*args):
#     print(args)
#     print(max(args) - min(args))
#     return sum(args)%2
# print(lovefunc(1,23,4))

# file = open("E:/Udemy Python/ALLCODINGexercises/Next Level Modules/smtp_module_udemy.py","w")


# ********************
# def are_you_playing_banjo(name):
#     return name + (' plays' if name[0].lower() == "r" else ' does not play') + ' banjo'

# print(are_you_playing_banjo("Rickie"))


# def check(seq,elem):
#     return elem in seq

# print(check([1,23,3,4,5,6,"ali"],'ali'))


# def string_to_array(s):
#     return s.split(" ")

# print(string_to_array("I love arrays they are my favorite"))


# toplam= 0
# i = 0
# while i < 1000:
#     toplam += i
#     i += 1
# print(toplam)


# a = 1
# b = 1
# liste = [a,b]
# liste2 = []
# for i in range(1000):
#     a,b= b,b+a
#     if b < 4000000:
#         liste.append(b)

# for i in liste:
#     if i % 2 != 0:
#         continue
#     else:
#         liste2.append(i)
# print(liste2)


# import sys
# max_val = sys.maxsize
# print(max_val)


# a = 'pyton is the best programming language ever!'
# liste = [*a]
# print(liste)
# liste = "".join(liste)
# print(liste)

# def lsit(*margs):
#     print(type(margs))
#     for i in margs:
#         pass
#     print(i)
# lsit(*liste)

# d,*b,c = liste
# print(d)
# print(b)
# print(c)

# print(liste[1::2])


# a,b,c,d,e =(1,2,3,4,5)
# print(a*b*c*d*e)
# print(b*a*c*d*e)
# print(c*a*b*d*e)
# print(d*e*a*b*c)
# print(e*a*b*c*d)


# def fonk(*args):
#     for arg in args:
#         print(arg)
# fonk(2)


# dict1 = {'color': 'blue', 'shape': 'square', 'volume':40}
# for i,j in dict1.items():
#     print(i,j)


# def our_decorator(func):
#     def function_wrapper(x):
#         print("Before calling " + func.__name__)
#         func(x)
#         print("After calling " + func.__name__)
#     return function_wrapper

# @our_decorator
# def foo(x):
#     print("Hi, foo has been called with " + str(x))

# foo('sie')


# def reverse_words(text):
#       return text[::-1]

# print(reverse_words('d c b a'))


# with open("e:/udemy python/allcodingexercises/pyqt5/notepad_project_udemy.py","w",encoding = "utf-8") as file:
#     file.write("import sys\nfrom PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout\n")


# def tup(*args):
#     print(type(args))
#     print(args)

# tup(1,2,3,4,5,5)


# file = open("e:/udemy python/allcodingexercises/pyqt5/homework_pyqt5_udemy.py","w",encoding = "utf-8")
# file.write("import requests\nfrom bs4 import BeautifulSoup")
# file.close()

# file = open("e:/udemy python/allcodingexercises/pyqt5/notepad_withmenubars_udemy.py","w",encoding="utf-8")
# file.write("selamu aleyk babba")
# file.close()


# for i in range(1000):
#     tot = 0
#     for j in range(1,i):
#         if i % j == 0:
#             tot+=j
#     if i == tot:
#         print(i)


# def randomdigits():
#     import random
#     randval = random.randint(3400000000000000,3499999999999999)
#     randval1 = random.randint(3700000000000000,3799999999999999)
#     randval2 = random.randint(4000000000000000,4999999999999999)
#     randval3 = random.randint(5100000000000000,5199999999999999)
#     randval4 = random.randint(6011000000000000,6011999999999999)
#     return randval, randval1, randval2, randval3, randval4

# def chklen(*args):
#     for i in args:
#         if len(str(i)) == 16:
#             return i
#     else:
#         return False

# print(chklen(*randomdigits()))

# def chklen(*args):
#     newlist = [i if len(str(i))==16 else False for i in args]
#     return newlist

# print(chklen(*randomdigits()))

# def chklen(*digits):
#     newlist = [i if len(str(i))==16 else False for i in digits]
#     return next(iter(newlist))
# print(chklen(*randomdigits()))


# from flask import Flask

# app = Flask(__name__)

# if __name__ == "__main__":
#     app.run(debug=True)

# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[j] == target - nums[i]:
#                     return [i, j]

# liste = Solution()
# f=[1,2,3,4,5]
# print(liste.twoSum(f,5))
# nums = [1,2,3,4,5,6]
# target = 11
# for i in range(len(nums)):
#           for j in range(i + 1, len(nums)):
#               if target == nums[j] + nums[i]:
#                   print([i, j])


# def twoSum(nums: list[int], target: int) -> list[int]:
#         hashmap = {}
#         for i in range(len(nums)):
#             hashmap[nums[i]] = i
#             print(hashmap)
# #         for i in range(len(nums)):
# #             complement = target - nums[i]
# #             if complement in hashmap and hashmap[complement] != i:
# #                 return [i, hashmap[complement]]
# print(twoSum(nums,target))

# nums = [1,2,3,4,5,6]
# target = 11

# hashmap = {}
# for i in range(len(nums)):
#     complement = target - nums[i]
#     if complement in hashmap:
#         print([i, hashmap[complement]])
#     hashmap[nums[i]] = i


# def add_binary(a, b):
#     return bin(a + b)

# print(add_binary(643,466))

# print(bin(3+2)[2:])

# s = "AdfajkflaA"
# print(list(enumerate(s)))

# import os
# newpath = "e:\\udemy python\\2.level\\templates"
# if not os.path.exists(newpath):
#     os.makedirs(newpath)

# def perfect(num):
#     total = 0
#     for i in range(1,num):
#         if num % i == 0:
#             total += i
#     if total == num:
#         print(f"This {num} Number Is Perfect")
#     else:
#         print("{} is not perfect".format(num))

# perfect(7)


# def tab():
#     for i in range(1,11):
#         for j in range(1,11):
#             print(f"{i}x{j}=",i*j)
#         print("\n","-----------","\n")
# tab()

# def armstrong(num):
#     i = num

# def perfect(x):
#     total = 0
#     for i in range(1,x):
#         if x % i == 0:
#             total += i
#     if total == x:
#         print("Number is Perfect")
#     else:
#         print("Not Perfect")
# perfect(6)


# my_set = [1,]
# for item in enumerate(my_set):
#     print(item ,end= " ")
# for index,value in enumerate(my_set):
#     print(item,value)


# print(4 or 2)
# print(4 and 2)


# print(True*3)


# a = [1,2,3]
# b = a
# b.append(4)
# print(a)


# greet = "hello",
# print(len(greet))


# a = "hello"
# print(a[::200])
# print(a[:100])


####### As ############
# first_number = input("Enter the first number:\t")
# second_number = input("Enter the second number:\t")
# try:
#     number1 = int(first_number)
#     number2 = int(second_number)
#     print(number1,"/",number2,"=",number1/number2)
# except (ValueError,ZeroDivisionError) as err:
#     print(f"some {err} occured")

#######  Raise ######
# dividend = int(input("enter the number: \t"))
# if dividend == 23:
#     raise Exception("No no no....Not 23...")
# divisor = int(input("Enter number for divisor:\t"))
# print(int(dividend/divisor))

#######  Raise ######
# try:
#     dividend = int(input("Enter the dividend:\v"))
#     divisor = int(input("Enter the divisor:\v"))
#     print(dividend/divisor)
# except ZeroDivisionError:
#     print("Cant divide a number to \"0\"")
#     raise


###### Assert #####
# name = input("enter your name:\v")
# assert len(name) != 0, "Input cant be empty"
# print(f"welcome {name}")


# l = [1,2,3,4,5]
# l.reverse()
# print(l)


# liste = [1,2,3,4,5]
# for i in range(len(liste)):
#     liste.pop()
# print(liste)


# liste = [1,2,3,4,5]
# liste1 = [liste.pop() for i in range(len(liste))]
# print(liste,liste1, sep = "\n")

# def concatenate(**kwargs):
#     res = ""
#     for i in kwargs:
#         res+= i
#     return res

# print(concatenate({"a":"python", "b":"real"}))


# files = {
# 'Input.txt': 'Randy',
# 'Code.py': 'Stan',
# 'Output.txt': 'Randy'
# }

# {'Stan': ['Code.py'], 'Randy': ['Output.txt', 'Input.txt']} # Ouput

# # def group_by_owners(files):
#     result = {key:[value] for (value,key) in files if key not in result}

# result= {}
# for key,value in files.items():
#     if value in result:
#         result[value].append(key)
#     else:
#         result[value]=[key]
# print(result)


# res = {}
# for i,j in files.items():
#     if j not in res:
#         res[j] = [i]
#     else:
#         res[j].append(i)
# print(res)

# nested_dict = {'first':{'a':1}, 'second':{'b':2}}
# flatted_list = dict()
# flatted = dict()
# for k,v in nested_dict.items():
#     for i,j in v.items():
#         flatted[k]=j
#         flatted_list[k]={j,i}
# print(flatted)
# print(flatted_list)


# trLetters = "abcdefgğhıijklmnoöprsştuüvyz"
# transTrLetters = {i:(trLetters.index(i) + 1) for i in trLetters}
# print(sorted("afgdhkıi", key = transTrLetters.get))


# fruit = "apple"
# fruit = "A" + fruit[1:]


# site1 = "www.google.com"
# site2 = "www.istihza.com"
# site3 = "www.gnu.com"
# site4 = "www.yahoo.com"

# for i in site1,site2,site3,site4:
#     print("http://",i[4:],sep="")


# import os; print(os.getcwd())


# x=7
# def f(x):
#   res=5
#   res*=res
#   if x%2==0:
#     print("Sonuc:",res)
#     return res
#   else:
#     print("Sonuc: ",res)

#     return res+10
# print(f(4))


# def f(x):
#     """bu fonksiyon parametlerin toplamini return eder.

#     Args:
#         x (int ): _description_
#     """
#     return x+x
# help(f)


# def consecutive(n):
#     """verilen n degerini n degeride dahil olmak uzere
#     yanyana bosluksuz dizip print eder.

#     Args:
#         n (int): range degerinde son aralik(inc)
#     """
#     print(*range(1,(n+1)),sep="")

# consecutive(12)


# st = """In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from a to m.

# The colors used by the printer are recorded in a control string. For example a "good" control string would be aaabbbbhaijjjm meaning that the printer used three times color a, four times color b, one time color h then one time color a...

# Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.

# You have to write a function printer_error which given a string will return the error rate of the printer as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.

# The string has a length greater or equal to one and contains only letters from ato z.

# Examples:
# s="aaabbbbhaijjjm"
# printer_error(s) => "0/14"

# # s="aaaxbbbbyyhwawiwjjjwwm"
# # printer_error(s) => "8/22"
# # """
# for harf in st:
#     print(r"{} harfi st paragrafinda {} kez geciyor".format(harf,st.count(harf)))

# for i in range(1,101):
#     for j in range(2,i+1):
#         if i % j == 0:
#             if i == j:
#                 print(i)
#             break


# a =[1,23,5,5,"essealmi"]
# for i in a:
#     if isinstance(i,(str)):
#         b = *i,
# print(b)


# def is_prime(x):
#     for i in x:
#         for j in range(2,i+1):
#             if i%j == 0:
#                 if i == j:
#                     print(i)
#                 break

# z = [*range(101)]
# print(is_prime(z))


#### Exception Chaining ####
# try:
#     a = int(input("sayi 1"))
#     b = int(input("sayi2"))
#     print(a/b)
# except (ZeroDivisionError,ValueError) as err:
#     raise TypeError (f"Burasi TypeError buda ZeroDivision Error hatasi:{err}") from err #bu hata olustugu icin bu hataya direct edildi print eder


# ##### Assert #######
# a = input("sayi girin:\v")
# assert len(a) != 0, "a is empty"
# print(int(a)*12)
# b = input("isim girin")
# assert isinstance(b,int), "b string"
# print(b*12)


# mailler={"kisi1":"ad1.soyad1@gmail.com","kisi2":"ad2.soyad2@gmail.com","kisi3":"ad3.soyad3@gmail.com"}
# l = []
# for v in mailler.values():
#     l.append(v)
# print(l)
# l = ",".join(l)
# print(l);print(type(l))


# a=20

# b=a

# a=a+5

# l=[20,30,40]

# l2=l

# l[0]=l[0]+5

# print(b,l2[0])


# def f(x,y=True):
#     if x%2 == 0:
#         y= False
#         return y
#     return y

# print(f(6,True))

# for i in range(1,101):
#     for j in range(2,i+1):
#         if i % j == 0:
#             if i == j:
#                 print(i)
#             break


# a = b= 1
# l = [a,b]
# for _ in range(1,123131231312313):
#     a,b = b,b+a
#     l.append(b)
# print(l)


#####################
# metin = "Bfjflrk öa kdhsı yteua idjslyd bdcusldvdj ks?"

# q_key = "qwertyuıopğüasdfghjklşi,zxcvbnmöç."
# f_key = "fgğıodrnhpqwuieaütkmlyşxjövcçzsb.,"

# trns = str.maketrans(q_key,f_key)

# # for i, j in trns.items():
# #     print(chr(i),chr(j))

# print(metin.translate(trns))
########################

# metin = """Bu programlama dili Guido Van Rossum adlı Hollandalı bir
# programcı tarafından 90'lı yılların başında geliştirilmeye başlanmıştır.
# Çoğu insan, isminin Python olmasına bakarak, bu programlama dilinin, adını
# piton yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu
# programlama dilinin adı piton yılanından gelmez. Guido Van Rossum bu
# programlama dilini, The Monty Python adlı bir İngiliz komedi grubunun, Monty
# Python's Flying Circus adlı gösterisinden esinlenerek adlandırmıştır. Ancak
# her ne kadar gerçek böyle olsa da, Python programlama dilinin pek çok yerde
# bir yılan figürü ile temsil edilmesi neredeyse bir gelenek halini almıştır
# diyebiliriz."""

# silinecek = "aeıioöuüAEIİOÖUÜ"

# # çeviri_tablosu = str.maketrans(silinecek,'_'*len(silinecek))
# # ceviri_tablosu_2 = str.maketrans('','',silinecek)

# # print(metin.translate(çeviri_tablosu))
# # print(metin.translate(ceviri_tablosu_2))

# newStr =""
# for i in metin:
#     if i not in silinecek:
#         newStr += i
# print(newStr)
#############################################

# a = "Besiktas Jimnastik Klubu"
# b = "".join(i for i in a if i.isalpha()).lower()
# print(b)
# ########################################

# print("cilek".encode("cp1254"))
#########

# Perfect

# def isPerfect(x):
#     """Sayiyi boldugunde sifir kalani veren kendine kadar olan sayilarin toplami eger sayinin kendine esitse bu fonksiyon True doner

#     Args:
#         x (int): 1,x

#     Returns:
#         str: Perfect or Not
#     """
#     tot = 0
#     for i in range(1,x):
#         if x % i == 0:
#             tot += i
#     if tot == x:
#         return(f"{x} is a Perfect Number")
#     return (f"{x} is not a Perfect Number")
# print(isPerfect(7))

################################
# for i in range(1,1000):
#     for j in range(2,i+1):
#         if i%j == 0 :
#             if i==j:
#                 print(i)
#             break


######################################
# import random
# *a,= "deneme123"
# b = tuple(a)
# print(a)
# print(b)
# random.shuffle(a)
# print(a)
######################################

# import random
# *a, = "deneme123"
# for i in range(len(a)-1,0,-1):
#     j = random.randint(0,i+1)
#     a[i],a[j] = a[j],a[i]
# print("Shuffled list is:",a)

####################################

# def iteleme(kaca_kadar):#1 kaliyor 2 list.remove
#     """
#     Halkadaki son numarayi yazin.1 den baslayip 2 yi egale edecek sekilde halka
#     verdiginiz son numaraya gore son 1 elemani kalacak sekilde sonlanacaktir.
#     Bu fonksiyon size listede kalan son kahramani gosterecektir.
#     """
#     liste = [*range(1,kaca_kadar)]
#     while len(liste) > 1:
#         last_item = liste[-1]
#         for i in liste[1::2]:
#             liste.remove(i)
#         if last_item in liste:
#             liste.pop(0)
#     return int(str(*liste))

# print(iteleme(40))

###############################
# li = [*range(1,1001)]
# while len(li) > 1 :
#     last_item = li[-1]
#     li = li[1::2]
#     if last_item not in li:
#         li.remove(li[1])
# print(li)

###################################
# def real_iteleme(kaca_kadar):
#     li = [*range(1,kaca_kadar)]
#     while 1 > len(li):
#         last_item = li[-1]
#         li = li[1::2]
#         if last_item not in li:
#             li.remove(li[1])
#     return li

# print(real_iteleme(11))
#######################################
# import random
# *a, = "deneme123"
# b = list(a) #or
# b = a[:]
# for _ in range(1,10):
#     for i in range(len(a)-1,0,-1):
#         j = random.randint(0,i+1)
#         a[i],a[j] = a[j],a[i]
#     for i in b:
#         if i not in a:
#             raise Exception("missing word")

#     print("Shuffled list is:",a)
# print(b)


#######################################
# def decorator(func):
#     def wrapper():
#         print(f"name of the function is {func.__name__}")
#         return func()
#     return wrapper

# @decorator
# def hi():
#     print("hello")

# hi()

# CLOSURE
# def outer():
#     msg = "hello world!" ## enclosing scope
#     def inner():
#         print(msg) ## local scope
#     return inner()
# outer()


##################################
# liste1 = [[1, 2, 3],
# [4, 5, 6],
# [7, 8, 9],
# [10, 11, 12],
# [13, 14, 15],
# [16, 17, 18],
# [19, 20, 21],
# [22, 23, 24],
# [25, 26, 27],
# [28, 29, 30],
# [31, 32, 33]]

# liste2 = [1, 27, 88, 98, 50, 9, 28, 45, 54, 66, 61, 23, 10, 33,
# 22, 12, 6, 99, 63, 26, 87, 25, 77, 5, 16, 93, 99, 44,
# 59, 69, 34, 10, 60, 92, 61, 44, 5, 3, 23, 99, 79, 51,
# 89, 63, 53, 31, 76, 41, 49, 10, 88, 63, 55, 43, 40, 71,
# 16, 49, 78, 41, 35, 97, 33, 76, 25, 81, 15, 99, 64, 20,
# 33, 6, 89, 81, 44, 53, 59, 75, 27, 15, 64, 36, 72, 78,
# 34, 36, 20, 41, 41, 75, 56, 30, 86, 46, 9, 42, 21, 64,
# 26, 52, 77, 65, 64, 12, 38, 1, 35, 20, 73, 71, 37, 35,
# 72, 38, 100, 52, 16, 49, 79]

# #######Created a 3 items sublist with list2's items
# liste3 = []
# li = []
# for i in liste2:
#     li.append(i)
#     if len(li) == 3:
#         liste3.append(li[:])#or li.copy() or list(li) which creates new id list.It is necessary because there is a deleting function down below so it will affect the appended list.
#         del(li[:])
# print(liste3)
# ############################

# for i in liste1:
#     ortak = [z for z in i if z in liste2]
#     if len(i) == len(ortak):
#         print(i)

#####################
# lst = [1,1,2,3,3,3,4,5,5]
# lst2 = [i for i in lst if i not in lst2]

# print(lst2)


##############################
# liste = ["alfred","toledo","tayfun","abc","cda","sa"]
# liste2 = ["dene","me","123"]
# # print(list(map(lambda x : x.upper(),liste)))
# # print(list(filter(lambda x:len(x)<5,liste)))
# # print(list(enumerate(liste)))
# print(list(zip(liste[::-1],liste2)))
# print(list(map(str.upper,liste)))

###############################
# for i in range(10,-1,-1):
#     print(i)

#############################
# def is_prime(x):
#     """prime number finder

#     Args:
#         x (list): returns list of prime number back
#     """
#     ls = list()
#     for i in x:
#         for j in range(2,i+1):
#             if i%j == 0:
#                 if i == j:
#                     ls.append(i)
#                 break
#     return ls

# print(is_prime([*range(101)]))
# ls = [(3,4),(10,3),(5,6),(1,9)]

# def rect_area(liste):
#     ls1 = [i*j for i,j in liste]
#     return ls1

# print(rect_area(ls))
# ls = [(3,4),(10,3),(5,6),(1,9)]
# print(list(map(lambda x : x[0]*x[1], ls)))


# files = {
# 'Input.txt': 'Randy',
# 'Code.py': 'Stan',
# 'Output.txt': 'Randy'
# }

# {'Stan': ['Code.py'], 'Randy': ['Output.txt', 'Input.txt']} # Ouput

# def func(files):
#     dic = {}
#     for key,value in files.items():
#         if value in dic:
#             dic[value].append(key)
#         else:
#             dic[value] = [key]
#     return print(dic)

# func(files)

# #Problem 63


# iterate multiple lists simultaneously
''' import itertools

num = [1,2,3]
color= ['red','white', 'black']
value = [255,256]

for i,j,k in zip(num,color,value): # zip()function stops when anyone of the list of all the lists gets exhausted.
    print(i,j,k) # will return 1 red 255; 2 white 256


for i,j,k in itertools.zip_longest(num,color,value): # stops when all lists are exhausted.When shorter iterators are exhausted,zip_longest yields a tuple with None value.
    print(i,j,k) # will return 1 red 255; 2 white 256; 3 black None

for i,j,k in itertools.zip_longest(num,value,color,fillvalue=-4444):# instead of None there will be fillvalue
    print(i,j,k) # will return 1 255 red; 2 256 white; 3 -4444 black '''

# lst = [1,2,3,4,'a',"bc"]
# a = enumerate(lst,1)
# i = iter(a)
# for _ in range(len(lst)): # _convention (ortak agiz)
#     print(next(i))

''' a = 123
b = "foo"
c = "bar"
print(dir())

for i in dir():
    if i.startswith("__") and i.endswith("__"):
        continue ##devam et asagi gecme (eger pass koysaydik code flowa gore if kosulu saglansa bile asagidaki kodu calistirip __ ile baslayan ve __ ile biten tum variable lari silecekti)
    del globals()[i]
del i
print(dir())
'''
# print('int','bin','len_bin',sep='\t')
# print('-'*len('int'),len('bin')*'-','-'*len('len_bin'),sep='\t')
# for i in range(11):
#     print(i,bin(i)[2:],len(bin(i)[2:]),sep='\t' )

# Decorator ex to understand local variable is accessible from global which defined in function
''' def changer(func):
    def wrapper(arg):
        func(arg)
        b = arg
        print(b)
    return wrapper

@changer
def func(arg):
    a= arg
    print(a)
    return a 

func(123)
print('outside')
'''

''' import requests
from bs4 import BeautifulSoup
response = requests.get(r"https://www.trendyol.com/")

soup = BeautifulSoup(response.content, 'html.parser')

links = soup.find_all('a')

for link in links:
    print(link.get("href"))
'''

# with open("/home/alice/Desktop/yazbel.pdf", "rb+") as file:
#     v = file.read()
# producer_index = v.index(b'/Producer')
# print(v[producer_index:producer_index+50])
# print(v[producer_index])


# with open("/home/alice/Desktop/The Pragmatic Programmer Your Journey to Mastery, 20th Anniversary Edition by Andrew Hunt David Hurst Thomas.pdf", "rb+") as file:
#     read = file.read()

# prod_index = read.index(b'/Producer')
# print(read[prod_index:prod_index+500])


# s = "ali cem koyun"
# print(s.index('cem'))

# l = [1,2,3,4,5]
# l[:3]=2
# print(*l)

''' def multiply(*args):
    global res
    res=1
    for i in args:
        res *= i
    print(res)
multiply(1,2,3,4)
print(dir()) '''

# print(*'TBMM', sep='.',end='.')
# import random

# def gener(start = 0, finish = 500, qty = 10):
#     number = set()

#     while len(number) < qty:
#         number.add(random.randrange(start,finish))
#     return number

# print(gener(5,144,10))
# print(len(gener(5,200,10))


# write a function that shows the prime numbers of list in range 0,1000

''' def prime_numbers(n):
    prime_list = []
    for num in range(2, n+1):
        is_prime = True
        for i in range(2, num):
            if (num % i == 0):
                is_prime = False
        if is_prime:
            prime_list.append(num)

    return prime_list


print(prime_numbers(1000))
'''
# for i in range(10):
#     if i == 5:
#         continue
#     print(i)


# print('selam\r\nas')


# a = int(input('sayi'))
# if a == 5:
#     raise 'what kinda error is that???'
#     print(asdf)


# byte = bytes('alicem', 'utf8')
# print(byte)
# st = str(byte, encoding='utf-8')
# print(st)


# import os
# print(callable(os.getcwd))

# lis = ['a', "bac"]
# print(lis)

# l = [i for i in range(10) if i/2 in (2,3,4)]
# print(l)


# print([i for i in range(10)if i%2 in (0,1)] == [i for i in range(10)])

# x = 123
# print(globals()['x'])
# globals().clear()
# print(globals())


# l = [*range(100), set('alicem'), {i: len(i) for i in ['alicem', 'koyun', 'deneme', "123"]}, frozenset('anutforajaroftuna')]
# print(l[:10:-1])

# print([*range(10)][-3:2:-1])


# l = [i if i % 2 != 0 else i % 2 == 1 for i in range(11)]
# print(l)


# for i in range(10):
#     if i % 2 == 1:
#         print([j for j in range(11)][::i])


''' 
import time

start = time.time()
for i in range(-1000,1000):
    for j in range(-1000,1000):
        if i is j:
            print(i)
print(time.time() - start)    # execution time 0.289991222
'''

''' import time

def gen(min,max):
    for i in range(min,max):
        yield i
        
start = time.time()
for i in range(-1000,1000):
    for j in gen(-1000,1000):
        if i is j:
            print(j)
print(time.time()-start) # exec time 0.357785224914 '''

# import random
# l = [random.randint(1,500) for _ in range(20)] # _ convention olsun diye bunu koyduk.
# print(l)


''' import random
l = [random.randint(1,1000) for _ in range(random.randrange(10,30))]
def tek(x):
    return x % 2 == 1
print('{} ogeden {} tanesi cift {} tanesi tek'.format(len(l),len(l)-len(list((filter(tek,l)))),len(list(filter(tek,l)))))
print('tek olanlar',*filter(tek,l)) '''

# import requests
# baseURL = 'https://swapi.dev/api/'
# get = requests.get(baseURL+'films/1/')

# dic = get.json()

# print(dic['title'])


# l = [1, 2, 3]


# def deneme(numara):
#     for i in l:
#         print(i * numara)


# print(deneme(2))

# # print(*map(lambda x:2*x,l))
# map(lambda x: x**2, l)


# d = {"dil": "language", "masa": "table",
#      "bilgisayar": "computer", "a": 1, "b": 2, "c": 3}

# a = list(d.values())
# b = list(d.keys())

# # if c:= input("deger girin") in a :
# #     print(b[a.index(c)])

# # sorgu = input("Gir")

# if sorgu := input("gir") in a:
#     print(b[a.index(sorgu)])
# print(sorgu)


# if walrus:=input("deneme"):
#     print(walrus)


# import inspect ## this module show the placeholders and their default values of functions

# print(inspect.signature(open)))

# print(5^3)


''' # sorted builtin function by key param
alp = "abcdefghijklmnoprstvwqxyz"
dct = {i: alp.index(i) for i in alp}

def sirala(kelime):
    return ([dct.get(kelime[i]) for i in range(len(kelime))])

#Example:
isimler = ["ahmet","mehmet","salih","alicem","koyun","metin zeki candan","michael schumacher"]

print(*sorted(isimler,key=sirala),sep="\n")
'''

# st, ls, dct, tup, stt = "alicem", [*"alicem"], dict.fromkeys(
#     (i for i in range(100)), "koyun"), (i for i in range(100)), {*"alicemkoyun"}
# print(isinstance(st, list)) #False
# print(isinstance(dct,dict)) #True

# print(vars(str))


# func = lambda x,y : x+y

# print(func(1,2))


# l = [1, 2, 3, 4, 5, 6]

# print(l[len(l)-1:])


# # Recursive Function Example
# n = 0
# def decrease(s):
#     global n
#     if len(s) < 1:
#         return s
#     else:
#         n+=1
#         print(list(s))
#         return decrease(s[1:])


# print(decrease("alicem"))


''' def decrease2(s):
    if len(s) < 1 or len(s) == 0:
        return s
    else:
        print(f"surec baslarken s:{s}")
        decrease2(s[1:])
        print(f"surec bittikten sonra s:{s}")

print(decrease2("alicem"))
'''

# import random
#
# for i in range(5):
#     l = [random.randint(random.randint(1, 1000), random.randint(1000, 5000)) \
#          for _ in range(random.randrange(1, 10), random.randrange(10, 20))]
#     print(*filter(lambda x: x % 2 == 0, l))

# def recursion(x):
#     if x == 0:
#         return x
#     else:
#         z = x+ recursion(x-1)
#     print(x)
#     return z
#
# print(recursion(500))


# def recursion(s):
#     if len(s) < 1:
#         return s
#     else:
#         print("before {}".format(s))
#         recursion(s[1:])
#         print(f"after {s}")
#
# recursion("anutforajaroftuna")

# ran = range(1,100)
# l = list(ran)
# l =(i if round(i/2)%2 == 0 else None for i in l )
# print("l = ",l)
# a,b,c,*d,e,f = l
# print(a,b,c,d,e,f, sep='\n')

# def ters(s):
#     if len(s) < 1:
#         return s
#     else:
#         return ters(s[1:]) + s[0]
#
#
# kelime = input("Ters kelime:\t")
# print("Girilen kelimenin tersi '{}'".format(ters(kelime)))
#

# def yazici():
#     a = 'deneme1'
#     print(a)
#     def yaz(msg):
#         nonlocal a
#         a = 'deneme2'
#         print(a)
#         def ciz(*args):
#             nonlocal a
#             a = 'deneme3'
#             print(a)
#         return ciz
#
#     return yaz
#
#
# yazici()('yazi tetikledi')('cizi tetikledi')


# def msg(msg):
#     msg = msg
#     print(msg)

# def func(msg):
#     def inner(sth):
#         print(msg+' Dunya')
#     return inner(msg)
# func('merhaba')

# a = 123
# def func():
#
#     global a
#     print(a)
#     a = 555
#     print(a)
#     def func2():
#         a = 75
#         print(a)
#     return func2()
# func()


# def banjo(name):
#     return name + (' plays' if name[0].lower() == 'r' else ' doesnt play') +\
#     ' banjo'
#
# print(banjo('Ricardo'))

# def outer(name):
#     def inner(surname):
#         print(surname, "Inner Func Worked")
#     return inner(name)
#
# print(outer('alicem')('koyun'))


# # Changing func name using variables
# def func(name='alicem'):
#     return name + f" Welcome, There are {len(name)} letter in your name"
#
#
# print(func(name=input("isim gir")))


# def topla(sayi):
#     if len(sayi) < 1:
#         return 0
#     else:
#         ilk, son = sayi[0], sayi[1:]
#         return ilk + topla(son)
#
#
# l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.11, 12]
#
# print(topla(l))


# # Flattening a list with recursion v_1
# def list_flatter(lst):
#     flattened_list = []
#     for element in lst:
#         if isinstance(element,list):
#             flattened_list.extend(list_flatter(element))
#         else:
#             flattened_list.append(element)
#     return flattened_list
#
# nested_list = [[1, 2, [3, 4]], [5, 6], 7, [8, [9, 10],[1]]]
# print(list_flatter(nested_list))
#

# l = [1,2,3]
# l.extend((1,))
# print(l)


# def ekle(*args):
#     eklenen = 0
#     for i in args:
#         eklenen += i
#
#     def bol(x, y):
#         nonlocal eklenen
#         eklenen += (x / y)
#         return eklenen
#     return bol
#
#
# a = ekle(1, 2, 3, 4)
# print(a(5,3))


# l = [*range(1_000_000)]
# def is_prime(x):
#     if x < 2:
#         return False
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             return False
#
#     return True
#
# def fillist (lst):
#     return list(filter(is_prime, lst))
#
# print(fillist(l))


# Fibonacci Series
# a =1
# b = 0
# for i in range(100):
#     a,b = b,a+b
#     print(a,b)


# def fibo_generator(treshold):
#     a = 1
#     b = 0
#     while b < treshold:
#         a, b = b, a + b
#         yield b
#
#
# # gen = fibo_generator
# # for i in gen(100):
# #     print(i)
# #Or
#
# iter_gen = iter(fibo_generator(100))
# print(next(iter_gen))


# def deneme(x):
#     print(x)

#     def deneme(x):
#         print(x)
#         deneme(x)
#     deneme(x)

# deneme('123')


# deneme: int = input('>>')
# print(type(deneme))


# arr = [1, 2, 3, 4, 1, 2, 3, 4]
# dc = dict.fromkeys(arr)
# print(dc, type(dc))
# print(list(dc))

'''def generator(sayi):
    for i in range(sayi):
        yield i
    return 


print(type(generator))
print(type(y := generator(5)))
print(y)
print(dir(generator))

for i in generator(11):
    print(i)'''


# my_iter = [i ** 2 if i != 2 else i*2 if i % 2 != 0 else i for i in range(10)]
# it = iter(my_iter)
# while True:
#     try:
#         git = next(it)
#         print(git)
#     except StopIteration:
#         break
# print(my_iter)



# def append_to_list(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         global ls
#         ls = list()
#         ls.extend([kwargs[j] for j in kwargs])
#         print('wrapper calisti')

#     return wrapper


# # @append_to_list
# def fibo(threshold: int, start=0, finish=None) -> int:
#     if not finish:
#         finish = start + 1
#     if finish:
#         if finish != start + 1:
#             print("In order to calculate Fibonacci series start and finish num\
#              bers normally should be consequitive")
#             if input("Do you want me the set it for you according to start ?\n y\
#                     or n ") == 'y' or "Y":
#                 finish = start + 1
#             else:
#                 pass

#     while finish < threshold:
#         start, finish = finish, start + finish
#         yield finish


# import time

# for i in fibo(100e100):
#     print(i)
#     s = time.time()
# print(time.time() - s, "ms surdu")


# def gen1():
#     for i in range(4):
#         yield i

# def gen2(number):
#     print(type(number))
#     for num in number:
#         yield num ** 2
        

# for i in gen2(gen1()):
#     print(i)



'''
a = dir(__import__('random'))

if 'a' in globals():
    print([i for i in globals()['a'] if not i.startswith('_')])
'''


'''
################ DECORATOR TEKRAR ####################
from functools import lru_cache, wraps
# to speed the process of calculating the factorials with recursion
from time import time
import sys


print('The recursion limiit is :',sys.getrecursionlimit())


def factorial(n):
    return n * factorial(n-1) if n else 1

start1 = time()
factorial(300)
finish1 = time() - start1

@lru_cache
def factorial2(n):
    return n * factorial2(n-1) if n else 1

start2 = time()
factorial2(300)
finish2 = time() - start2

print(f'Normal kullanim {finish1}--Cacheli kullanim {finish2}')
print(f'@lru_cache normal kullanima gore {finish1 - finish2} daha hizli')

# wraps kullanim ornegi
def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator cagrildi Wraps'ten selamlar!!")
        return func(*args, *kwargs)
    return wrapper

@decorator
def deneme(x):
    """deneme yapar

    Args:
        x (str): str doner decorator kullanimi
    """
    print(x)

deneme("selam")
help(deneme) # @wraps doctrings i silmez korur ama diger turlu decorator kullanimi docstr siler.
'''

# def dec(le):
#     def decorator(func):
#         def wrapper():
#             print(le, func())
#         return wrapper
#     return decorator


# @dec('foo')
# def foo():
#     return('bar')

# foo()



'''
def decorator(y):
    def deco(func):
        def wrapper(*args, **kwargs):
            i,= args
            func(i*y)
        return wrapper
    return deco

@decorator(5)
def bati(x):
    if x % 2 == 0:
        print(f"{x} cift sayi")
        x = x + 1
        print(f'{x} tek sayi oldu artik')
    else:
        print(f'{x} cift sayi degil ki yaaaa')


from functools import wraps

##################################################
def my_decorator(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('sth happened before function call')
        func(*args, **kwargs)
        print('sth happened after function call')
    return wrapper

@my_decorator
def example_function():
    """
    "This is the docstring of the example function
    """
    print("Example function is executed")
    
example_function()
print(example_function.__doc__)
print(example_function.__name__)
'''

# import logging

# logging.info("say something Iam givin up on you")

"""
x = 11

def deneme():
    x = 22
    print(x)
    
def deneme2():
    x = 33
    print(x)

def deneme3():    
    global x 
    x = 'global2'

deneme();deneme2();deneme3()

print(locals())
print(globals())

"""

