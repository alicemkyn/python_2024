'''
- **1xx Informational**
  - 100 Continue
  - 101 Switching Protocols
  - 102 Processing (WebDAV)
  - 103 Early Hints

- **2xx Successful**
  - 200 OK
  - 201 Created
  - 202 Accepted
  - 203 Non-Authoritative Information (since HTTP/1.1)
  - 204 No Content
  - 205 Reset Content
  - 206 Partial Content
  - 207 Multi-Status (WebDAV)
  - 208 Already Reported (WebDAV)
  - 226 IM Used

- **3xx Redirection**
  - 300 Multiple Choices
  - 301 Moved Permanently
  - 302 Found
  - 303 See Other (since HTTP/1.1)
  - 304 Not Modified
  - 305 Use Proxy (since HTTP/1.1)
  - 306 Switch Proxy
  - 307 Temporary Redirect (since HTTP/1.1)
  - 308 Permanent Redirect (RFC 7538)

- **4xx Client errors**
  - 400 Bad Request
  - 401 Unauthorized
  - 402 Payment Required
  - 403 Forbidden
  - 404 Not Found
  - 405 Method Not Allowed
  - 406 Not Acceptable
  - 407 Proxy Authentication Required
  - 408 Request Timeout
  - 409 Conflict
  - 410 Gone
  - 411 Length Required
  - 412 Precondition Failed
  - 413 Payload Too Large
  - 414 URI Too Long
  - 415 Unsupported Media Type
  - 416 Range Not Satisfiable
  - 417 Expectation Failed
  - 418 I'm a teapot (RFC 2324)
  - 421 Misdirected Request (RFC 7540)
  - 422 Unprocessable Entity (WebDAV)
  - 423 Locked (WebDAV)
  - 424 Failed Dependency (WebDAV)
  - 425 Too Early (RFC 8470)
  - 426 Upgrade Required
  - 428 Precondition Required (RFC 6585)
  - 429 Too Many Requests (RFC 6585)
  - 431 Request Header Fields Too Large (RFC 6585)
  - 451 Unavailable For Legal Reasons

- **5xx Server errors**
  - 500 Internal Server Error
  - 501 Not Implemented
  - 502 Bad Gateway
  - 503 Service Unavailable
  - 504 Gateway Timeout
  - 505 HTTP Version Not Supported
  - 506 Variant Also Negotiates (RFC 2295)
  - 507 Insufficient Storage (WebDAV)
  - 508 Loop Detected (WebDAV)
  - 510 Not Extended (RFC 2774)
  - 511 Network Authentication Required

'''

import requests

r = requests.get('https://httpbin.org')
r_methods = [i for i in dir(r) if not i.startswith('_')]

print(r_methods, '\nLen:', len(r_methods))
#help(r)


# get request to image urls with text and content methods
r = requests.get('https://imgs.xkcd.com/comics/python.png')
print(r.text)
print(r.content) # byte code 

# to download it
with open('comics.png', 'wb') as f:
    f.write(r.content)

# status code check
print(r.status_code) # 200 OK!


# headers
print(r.headers)
'''
Output:
{
    'Connection': 'keep-alive', 'Content-Length': '90835', 'Server': 'nginx', 
    'Content-Type': 'image/png', 'Last-Modified': 'Mon, 01 Feb 2010 13:07:49 GMT', 
    'ETag': '"4b66d225-162d3"', 'Expires': 'Mon, 05 Feb 2024 07:39:12 GMT', 
    'Cache-Control': 'max-age=300', 'Accept-Ranges': 'bytes', 
    'Date': 'Mon, 05 Feb 2024 13:09:51 GMT', 'Via': '1.1 varnish', 
    'Age': '144', 'X-Served-By': 'cache-vie6320-VIE', 'X-Cache': 'HIT', 
    'X-Cache-Hits': '1', 'X-Timer': 'S1707138591.322318,VS0,VE1'
    }
'''


# Try methods with httpbin.org
url = 'https://httpbin.org/get'
payload = {'page': 2 , 'count': 25}

r = requests.get(url=url, params=payload)
print(r.text)
'''
Response:

{
  "args": {
    "count": "25", 
    "page": "2"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.31.0", 
    "X-Amzn-Trace-Id": "Root=1-65c0dfc9-2150d5d743be20e54affbd53"
  }, 
  "origin": "88.238.48.197", 
  "url": "https://httpbin.org/get?page=2&count=25"
}
'''

print(r.url) # https://httpbin.org/get?page=2&count=25


#post request
url = 'https://httpbin.org/post'
form = {'username': 'alicemkyn', 'password': 'testing'}

r = requests.post(url=url, data=form)

print(r.text)
print(r.json()) # Returns dict

r_dict = r.json()
print(r_dict['form']) # {'password': 'testing', 'username': 'alicemkyn'}


#Logins and Authentications with credentials
#go and check the documentation on https://httpbin.org
url = 'https://httpbin.org/basic-auth/alicemkyn/testing'

while True:
    username = input('Enter Username: ')
    password = input('Enter Password: ')
    r = requests.get(url=url, auth=(username, password))
    
    if r.status_code // 100 == 4:
        print('You enter wrong username or password. Please try again!')
    else:
        print('Enter is successfull...Redirecting')
        print(r.text)
        break


# Dynamic data delay testing timeout
r = requests.get('https://httpbin.org/delay/1', timeout=3)
print(r) # <Response [200]>

r = requests.get('https://httpbin.org/delay/4', timeout=3)
print(r) # ReadTimeout exception

