'''
* We can run different tasks concurrently.
* CPU bound tasks = They are crunching a lot of numbers and using CPU.
* I/O bound tasks = They are things that are just waiting for input and
output operations to be completed and not really using the CPU all that
much.
* We are going to see the benefits of using threading when our tasks are
I/O bound to not wait the operations finished.
* If our task is CPU bound then we'll likely want to use multiprocessing
module and run the processes parallel instead.
* _ in for loop means throw away variable.
'''
import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')
lg = logging.debug


# Using without the threading module
start = time.perf_counter()

def do_something():
    lg('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

do_something()
do_something()

finish = time.perf_counter()
print(f'Finished in {round(finish - start, 2)} second(s).') # 2.01 sec

'''
Output:
Sleeping 1 second...
Done Sleeping...
Sleeping 1 second...
Done Sleeping...
Finished in 2.01 second(s).
'''


# Using the same code with threading
start = time.perf_counter()

def do_something():
    lg('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')
    
# Instead of calling function twice we'll use threading
# do_something()
# do_something()
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()

finish = time.perf_counter()
print(f'Finished in {round(finish - start, 2)} second(s).')
'''
Output:
Sleeping 1 second...
Sleeping 1 second...
Finished in 0.0 second(s).
Done Sleeping...
Done Sleeping...
'''

# join() method
start = time.perf_counter()

def do_something():
    lg('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')
    
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start() # Starts simultanously with t2
t2.start()

t1.join() # Wait for the complete t1 and t2 finish their job before executing next line(finish)
t2.join() 

finish = time.perf_counter()
print(f'Finished in {round(finish - start, 2)} second(s).')
'''
Output:
Sleeping 1 second...
Sleeping 1 second...
Done Sleeping...
Done Sleeping...
Finished in 1.01 second(s).
'''

# if we want to create 10 threads instead use loop
start = time.perf_counter()

def do_something():
    lg('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

threads = []

for _ in range(10):
    t = threading.Thread(target=do_something)
    t.start()
    threads.append(t) # We cant use join() in loop so we add it to the list then use join() in other for loop for created threads    

for thread in threads:
    thread.join()

finish = time.perf_counter()
print(f'Finished in {round(finish - start, 2)} second(s).')
# Finished in 1.01 second(s). (Normally it would take the 10 seconds.)


# Using Threads with function that has args, and how to pass args to threads.
start = time.perf_counter()

def do_sth(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('Done Sleeping...')

threads = list()

for _ in range(10):
    t = threading.Thread(target=do_sth, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()
print(f'Finished in {round(finish - start, 2)} second(s)...')
# Finished in 1.51 second(s)...


############### New Way of Using Threads >= Python 3.2 #################
import concurrent.futures

start = time.perf_counter()

def do_sth(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return 'Done Sleeping...'

#Using with context manager
with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(do_sth, 1) #submit(function,args) -> returns future object
    print(f1.result()) #f1 is an object and with result() method it will actually wait around until the function completes to see the results.

finish = time.perf_counter()
print(f'Finished in {round(finish - start, 2)} second(s)...')



# as_completed() method
#Using it with for loop to use it multiple times(I will use list comprehension)
start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(do_sth, 1) for _ in range(10)]
    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()
print(f'Finished in {round(finish - start, 2)} second(s)...')
# Finished in 1.01 second(s)...


# Another example:
start = time.perf_counter()

def do_sth(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = [executor.submit(do_sth, sec) for sec in secs]
    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()
print(f'Finished in {round(finish - start, 2)} second(s)...')
'''
Output: Because of the as_completed() 1 sec is first completed so it prints first
Done Sleeping...1
Done Sleeping...2
Done Sleeping...3
Done Sleeping...4
Done Sleeping...5
Finished in 5.01 second(s)...
'''

# Now lets use the example above with map() to get rid of the for loop and list comprehension above
# map() and ThreadPoolExecutor().map() is different but syntax is same and they do the same thing.
start = time.perf_counter()

def do_sth(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_sth, secs) # map() method here
    for result in results:
        print(result)

finish = time.perf_counter()
print(f'Finished in {round(finish - start, 2)} second(s)...')
'''
Output: map() will return the results in the order that they were started.
Done Sleeping...5
Done Sleeping...4
Done Sleeping...3
Done Sleeping...2
Done Sleeping...1
Finished in 5.01 second(s)...
'''