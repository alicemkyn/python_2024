'''
https://httpbin.org/

It echoes the data used in your request for any of these types:

https://httpbin.org/anything Returns most of the below.
https://httpbin.org/ip Returns Origin IP.
https://httpbin.org/user-agent Returns user-agent.
https://httpbin.org/headers Returns header dict.
https://httpbin.org/get Returns GET data.
https://httpbin.org/post Returns POST data.
https://httpbin.org/put Returns PUT data.
https://httpbin.org/delete Returns DELETE data
https://httpbin.org/gzip Returns gzip-encoded data.
https://httpbin.org/status/:code Returns given HTTP Status code.
https://httpbin.org/response-headers?key=val Returns given response headers.
https://httpbin.org/redirect/:n 302 Redirects n times.
https://httpbin.org/relative-redirect/:n 302 Relative redirects n times.
https://httpbin.org/cookies Returns cookie data.
https://httpbin.org/cookies/set/:name/:value Sets a simple cookie.
https://httpbin.org/basic-auth/:user/:passwd Challenges HTTPBasic Auth.
https://httpbin.org/hidden-basic-auth/:user/:passwd 404'd BasicAuth.
https://httpbin.org/digest-auth/:qop/:user/:passwd Challenges HTTP Digest Auth.
https://httpbin.org/stream/:n Streams n–100 lines.
https://httpbin.org/delay/:n Delays responding for n–10 seconds.

'''
import concurrent.futures
import threading
import requests
import logging
import time

logging.basicConfig(level=logging.DEBUG, format='%(message)s')


url = 'https://httpbin.org/post'

data = {
    'name':'alicem',
    'surname':'koyun',
    'city':'Ankara',
    'country':'Turkey'
}
counter = 0

def do_request():
    start = time.perf_counter()
    while True:
        response = requests.post(url, data=data).text

        logging.debug(response)
        global counter
        counter += 1
        # logging.debug(counter)
        if round(time.perf_counter() - start) >= 10:
            logging.debug(counter)
            break

threads = []

for i in range(50):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()
    
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     for _ in range(50):
#         executor.submit(do_request)