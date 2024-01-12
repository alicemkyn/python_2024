import datetime 
import pytz

# datetime.date (year-month-day only)
d = datetime.date(2016,7,24)
print(d) # 2016-07-24

tday = datetime.date.today()
print(tday)# 2024-01-11
print(tday.year) # 2024
print(tday.day) # 11
print(tday.weekday()) # 3 # Mon=0.....Sun=6

# To find the date after some days from now
tdelta = datetime.timedelta(days=7) # e.g. 7 days later from now on.
print(tday + tdelta) # 2024-01-18 which is 7 days later.
print(tday - tdelta) # 2024-01-04 which is 8 days ago.

# To calculate how many days left till my birthday.
bday = datetime.date(2024,7,31) # Careful, no zeros before month digit.
till_bday = bday - tday
print(till_bday) # 202 days, 0:00:00
print(till_bday.days) # 202
print(till_bday.total_seconds()) # This is a method # 17452800.0


#datetime.time (hours-minutes-seconds-microseconds only)
t = datetime.time(9, 30, 45, 100000) #hours-minutes-seconds-microseconds
print(t) # 09:30:45.100000
print(t.hour) # 9


# datetime.datetime !We will access everything! Both above.
dt = datetime.datetime(2024,1,11, 12,30,45,100000)
print(dt) # 2024-01-11 12:30.45.100000
print(dt.date()) # 2024-01-11
print(dt.time()) # 12:30:45.100000
print(dt.year) # 2024

tdelta1 = datetime.timedelta(days=7)
print(dt + tdelta1) # 2024-01-18 12:30:45.100000
tdelta2 = datetime.timedelta(hours=12)
print(dt + tdelta2)# 2024-01-12 00:30:45.100000

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()
print(dt_today) # 2024-01-11 19:11:31.305442
print(dt_now) # 2024-01-11 19:11:31.305444
print(dt_utcnow) # 2024-01-11 16:11:31.305495
# Here I installed pytz which is recommended even in Python's datetime
# documentation on their official site.(Timezone module). Imported pytz

dt1 = datetime.datetime(2024,1,11, 12,30,45, tzinfo=pytz.UTC)
print(dt1) # 2024-01-11 12:30:45+00:00 (+00:00 UTC Offset)
dt1_now = datetime.datetime.now(tz=pytz.UTC)
print(dt1_now) # 2024-01-11 16:21:48.978519+00:00
dt1_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt1_utcnow) # 2024-01-11 16:24:01.640128+00:00
# dt1_now and dt1_utcnow is the same but we will use the dt1_now because
# there is less to write and easy to remember and use.

dt2_utcnow = datetime.datetime.now(tz=pytz.UTC)
dt_mtn = dt2_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn) # 2024-01-11 09:33:18.565409-07:00
dt_ist = dt2_utcnow.astimezone(pytz.timezone('Europe/Istanbul'))
print(dt_ist) # 2024-01-11 19:38:22.768815+03:00

# To see all timezone list for other locations or just option+click module
for tz in pytz.all_timezones:
    print(tz)

# To make naive datetime timezone aware
dt_ist1 = datetime.datetime.now()
print(dt_ist1) # Current true local time but not aware of timezone 
# 2024-01-11 19:48:23.332613
# If I want to convert Istanbul's timezone to Canada timezone
dt_can = dt_ist1.astimezone(pytz.timezone('Canada/Pacific'))
print(dt_can) # 2024-01-11 08:52:32.421970-08:00
# OR
ist_tz = pytz.timezone("Europe/Istanbul")
dt_ist2 = ist_tz.localize(dt_ist1)
print(dt_ist2) # Current true local time but now aware of timezone
# 2024-01-11 19:58:03.179919+03:00
dt_can2 = dt_ist2.astimezone(pytz.timezone('Canada/Pacific'))
print(dt_can2) # Same result 2024-01-11 09:00:56.677394-08:00

# To create clean timezone aware local time
dt_istanbul = datetime.datetime.now(tz=pytz.timezone('Europe/Istanbul'))
print(dt_istanbul) # 2024-01-11 20:03:10.531879+03:00




################## DATETIME FROM MY POINT OF VIEW ######################
moment = datetime.datetime.now() # datetime.datetime.today()- both same
print(
    moment.year, 
    moment.month, 
    moment.day, 
    moment.hour, 
    moment.minute,
    moment.second,
    moment.microsecond,
    sep ='\n'
    ) # 2024,1,12,15,42,56,711759



# ctime()
'''Returns readable date and time in str format
takes an object as an argument which returns from now() method.'''

dat = datetime.datetime.ctime(moment)
print(dat) # 'Fri Jan 12 15:53:26 2024'




# strftime()
''' This methods provides us to format and use date and time 
information. Its first argument is same as in ctime() method takes the
object instantiated from now() class,additionally it takes special 
formatting characters as a second argument.
%a - abbreviation of day
%A - full name of day
%b - abbreviaton of month
%B - full name of month
%c - full information of date and time
%d - numeric day in str format
%j - which is the current day in range of 0-366
%m - numeric month in str format
%U - shows the number of the week in current year in range of 0-53
%y - last two digit of the year
%Y - all digits of the year
%x - full date info e.g. '05/02/23'
%X - full time info e.g. '11:50:15'
AM Ante Meridiem - Before Midday (12:00night - 11:59noon)
PM Post Meridiem - After Midday (12:00noon - 11:50night)
'''
dte = datetime.datetime.strftime(moment, '%c')
print(dte) # 'Fri Jan 12 16:26:11 2024'

# What if we want to get them in the different language?
import locale
locale.setlocale(locale.LC_ALL, 'tr_TR')

dte = datetime.datetime.strftime(moment, '%B')
print(dte) # 'Ocak'

dte = datetime.datetime.strftime(moment, '%d %m %Y tarihinde bulusalim')
print(dte) # '12 01 2024 tarihinde bulusalim'




#strptime()
tme = '27 Mayis 2016'
gun, ay, yil = tme.split()
print(gun, ay, yil)

# What if we have sth like that ?
tme = '27 Mayis 2016 saat 12:34:44'
gun,ay,yil,saat = [i for i in tme.split() if i != 'saat']
print(gun,ay,yil,saat)

# We can do the same process above with the strptime() method easily and
# use them with datetime.datetime as an object.
tt = '27 Mayıs 2016 saat 12:34:44' # Mayis set localeden dolayi 'ı'oldu.
z = datetime.datetime.strptime(tt, '%d %B %Y saat %H:%M:%S')
print(z) # 27 Mayis 2016 12:34:44 <class 'datetime.datetime'>
print(
    z.month,
    z.year,
    z.day,
    z.hour,
    z.minute,
    z.second,
    sep='\n'
) # 5 2016 27 12 34 44



#fromtimestamp()
'''e.g os.stat('filename') l-> returns the status of the file.
os.stat('filename').st_mtime -> returns timestamp 1417784445.8881965
This method is used for the convertion of this timestamp to normal date.
Takes epoch time as an argument. We know that epoch time is a seconds
that have passed from 01/01/1970 till now.'
'''
import os 
locale.setlocale(locale.LC_ALL, '') # set locale back to computers default

t_stamp = os.stat('.gitignore').st_mtime
conv_date = datetime.datetime.fromtimestamp(t_stamp)
print(conv_date) # 2024-01-11 17:49:39.225657 <class 'datetime.datetime'>

readable_date = datetime.datetime.strftime(conv_date, '%c')
print(readable_date)# 'Thu Jan 11 17:49:39 2024' #eng cuz locale setted default



#timestamp()
'''We use this method to generate timestamp in type of epoch time'''
cur_dt = datetime.datetime.now()
tm_stamp = datetime.datetime.timestamp(cur_dt)
print(tm_stamp) # 1705071331.259766 (float) (epoch time)
# To convert it back to normal readable date we can use again fromtimestamp()




################# ARITHMETICAL OPERATIONS WITH DATES ###################
'''Instead of taking the current date with now() and today() methods
we can set any date we want.
Time delta means the difference between two dates.
'''
a = datetime.datetime(2023,5,3,10,37,53) # yy:m:d:h:m:s
print(
    a.year,
    a.month,
    a.day,
    a.hour,
    a.minute,
    a.second,
    sep='\n'
)


# To calculate the difference between two different dates
bugun = datetime.datetime.today()
d_gunu = datetime.datetime(1989,7,31)
fark = bugun - d_gunu # datetime.timedelta object
print(fark) # 12583 days, 18:31:50.477290 <class 'datetime.timedelta'>
print(
    fark.days,
    fark.seconds,
    fark.microseconds
    ) # int > 12583 66667 568992


# To find a future date
''' We will use timedelta object for this.
Instead of subracting two dates and finding datetime.timedelta, 
we will set it manually.
'''
bugun = datetime.datetime.today()
fark = datetime.timedelta(days=200)
gelecek = bugun + fark # datetime.datetime object
print(
    gelecek.year,
    gelecek.month,
    gelecek.day,
    gelecek.hour,
    gelecek.minute,
    gelecek.second,
    gelecek.microsecond,
    sep='-'
) # int -> 2024-7-30-18-38-19-518327
print(gelecek.strftime('%c')) # 'Tue Jul 30 18:35:39 2024'


# To find a past date
bugun = datetime.datetime.today()
fark = datetime.timedelta(days=200)
gecmis = bugun - fark # datetime.datetime object
print(gecmis.strftime('%c')) # Mon Jun 26 18:40:19 2023
