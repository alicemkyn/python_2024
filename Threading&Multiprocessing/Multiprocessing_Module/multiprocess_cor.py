import multiprocessing
import concurrent.futures
import time
import logging
import os

"""
Everything is the same with threading module, instead we only write Process
for Thread and in concurrent.futures module while using context manager we use
ProcessingPoolExecutor() instead ThreadingPoolExecutor().
Here every process has its own GIL. If we have 4 physical cores and 4 virtual
cores (total 8) we can calculate it if we don't have any clue about it with os.cpu_count().

* IF WE HAVE 8 CORES TOTAL THAT MEANS THAT WE CAN CREATE
8 PROCESSES CONCURRENTLY.
"""

logging.basicConfig(level=logging.DEBUG, format='%(message)s')
lg = logging.debug


def do_something():
    lg('Sleeping 1 second...')
    time.sleep(1)
    lg('Done sleeping...')
    return 'I still feel sleepy...'
    

if __name__ == '__main__':
    start = time.perf_counter()
    
    # p1 = multiprocessing.Process(target=do_something)
    # p2 = multiprocessing.Process(target=do_something)

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()
    
    processes = []
    
    for _ in range(10):
        p1 = multiprocessing.Process(target=do_something)
        # if we defined it with a parameter then:
        # p1 = multiprocessing.Process(target=do_something, args=[1.5])
        p1.daemon = True
        processes.append(p1)
    
    for i in range(10):
        processes[i].start()
    
    for i in range(10):
        processes[i].join()
    

    finish = time.perf_counter()
    lg(f'Finished in {round(finish - start, 2)} second(s)') # 1.08 sec
    


#################### Using ProcessPoolExecutor #########################

if __name__ == '__main__':
    
    start = time.perf_counter()
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # to execute once; f1 = executor.submit(func, arg) -> futures obj.(f1)
        # f1.result() -> return value of function -> I still feel sleepy...
        # to use in loop (not create an empty list and append it in loop)
        results = [executor.submit(do_something) for _ in range(10)]
        # concurrent.futures.as_completed(results) -> iterator
        for f in concurrent.futures.as_completed(results):
            print(f.result())
    
    finish = time.perf_counter()
    lg(f'Finished in {round(finish - start, 2)} second(s)') # 2.09 sec


def do_something2(second):
    lg(f'Sleeping {second} second(s)...')
    time.sleep(second)
    return f'Done Sleeping...{second}'

if __name__ == '__main__':
    start = time.perf_counter()
    
    with concurrent.futures.ProcessPoolExecutor() as exc:
        secs = [*range(1,6)]
        results = [exc.submit(do_something2, sec) for sec in secs]
        for f in concurrent.futures.as_completed(results):
            lg(f.result())
    
    finish = time.perf_counter()
    lg(f'Finished in {round(finish - start, 2)} second(s)...') # 5.08 sec


######### Map method

if __name__ == "__main__":
    
    start = time.perf_counter()
    
    with concurrent.futures.ProcessPoolExecutor() as exc:
        secs = [*range(1,6)]
        results = exc.map(do_something2, secs)#-> results in the order they were started
        for i in results:
            lg(i)
    # If our function raises an exception it won't actually raise an exception
    # while running the process the exception will be raised when its return value
    # retrieved from the results iterator. So it will be a good idea to handle with
    # exceptions in the for loop above. Because this is the place that we retrieve
    # the results from our results iterator.
    
    finish = time.perf_counter()
    lg(f'Finished in {round(finish - start, 2)} second(s)...') # 5.08 sec





############## USING THREADING WITHIN MULTIPROCESSING ##################

import threading, multiprocessing, requests, os, logging,time

logging.basicConfig(level=logging.DEBUG, format='%(message)s')
lg = logging.debug

# https://httpbin.org/post ' a requests ile datamizi post 
# os.cpu - process sayimizi belirleyecegiz
# her processimizin icinde 50 tane thread calistiracagiz

url = 'https://httpbin.org/anything'

data = {
    'name': 'Kyle',
    'surname': 'Petrovski',
    'age': 42
}

post_counter = 0

def do_request():
    start = time.perf_count()
    while True:
        response = requests.post(url, data=data).text
        lg(response)
        global post_counter
        post_counter += 1
        # lg(post_counter)
        if round(time.perf_counter - start) == 10:
            lg(post_counter)
            break
        

def call_thread(number, function, *args):
    threads = []
    for _ in range(number):
        t = threading.Thread(target=function, args=args)
        t.daemon = True
        threads.append(t)
    
    for i in range(number):
        threads[i].start()
    
    for i in range(number):
        threads[i].join()

if __name__ == "__main__":
    processes = []

    for _ in range(os.cpu_count()):
        p = multiprocessing.Process(target=call_thread, args=(50, do_request))
        p.daemon = True
        processes.append(p)

    for process in processes:
        process.start()

    for process in processes:
        process.join()
