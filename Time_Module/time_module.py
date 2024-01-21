'''
* Same attrs and methods from datetime package. 
* Same process steps with datetime package.
* Time module works with hours only.
'''
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')
lg = logging.debug

# 1- gmtime() 
lg(time.gmtime()) # time.struct_time(tm_year=2024, tm_mon=1, tm_mday=21, tm_hour=18, tm_min=30, tm_sec=14, tm_wday=6, tm_yday=21, tm_isdst=0) # Current time UTC 0
lg(time.gmtime(0)) # time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0) # EPOCH time

# 2- time()
'''
Returns the current time in seconds since the epoch 
(January 1, 1970, 00:00:00 UTC). It is a floating-point value 
representing the number of seconds that have passed since that reference
point. This function is commonly used for measuring elapsed time or for 
timestamping events.
'''
lg(time.time()) # 1705862862.3206651

# 3- localtime()
lg(time.localtime()) # time.struct_time(tm_year=2024, tm_mon=1, tm_mday=21, tm_hour=21, tm_min=50, tm_sec=38, tm_wday=6, tm_yday=21, tm_isdst=0)

# 4- asctime()
lg(time.asctime()) # Sun Jan 21 21:51:42 2024 # UTC+3 correct local time
lg(time.asctime(time.gmtime())) # Sun Jan 21 18:52:53 2024 # UTC 0
lg(time.asctime() == time.asctime(time.gmtime())) # False
lg(time.asctime(time.gmtime(0))) # Thu Jan  1 00:00:00 1970

tup = (2029, 7, 31, 00,00,00, 0,0,0)
lg(time.asctime(tup)) # Mon Jul 31 00:00:00 2029

# 5- strftime()
lg(time.strftime('%c')) # Sun Jan 21 22:01:36 2024 # Current local date
# Date formatters in datetime package are the same and available for time module.
# %a, %A, %b, %B, %c, %d, ....

# 6- strptime() #same in datetime package.
d = '31 July 2029'
dt = time.strptime(d, '%d %B %Y')
lg(dt) # time.struct_time(tm_year=2029, tm_mon=7, tm_mday=31, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=212, tm_isdst=-1)
# This returns time.struct object
# Datetime package returns datetime.datetime object.


# 7- sleep() # Takes arg in seconds type
time.sleep(0.001)