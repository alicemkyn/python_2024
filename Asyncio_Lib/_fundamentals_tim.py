'''
SYNTAX:
- async def -> classical function define but with async (coroutine)
- synchronous functions don't work in async functions. 
- await works only in def block. NOT outside of the async function definiton.
- await runs only coroutine object. 
- asynchronoulsy defined function is an coroutine object.
- we cant call them like we call vanilla python function.
- we need to run them using coroutine objects methods. e.g asyncio.run(func())
- Advantage of using asyncio is gather() method.
asyncio.gather(async_func1(), async_func2(), async_func2()) OR
asyncio.gather(async_func1, *[async_func2() for _ in range(3)])
we created list comprehesion of async function and unpacked it.
If functions that gather executes return a value we need to assing gather
to variable and store the return values.Then we can print it. It returns
values in list.
- asyncio.to_thread(func, arg_of_func(*args, **kwargs)) -> This converts
the sync func into async function.
e.g. asyncio.gather(*[asyncio.to_thread(func) for _ in range(50)])




- async function icerisinde neden senkron bir fonksiyon calistirmaz
cunku async function await kismina geldiginde await komutunun sagindaki
kod bir coroutine objesi olusturur ve bunu event loop kuyruguna takar.
Bu sirada bu kod bekleme suresine gecerse yani bu kodu calistiran threadi
bosa cikarirsa thread hemen schedule ettigi baska varsa async islemleri calisitirmaya gecer ama event
loop kuyrugunda oldugu icin bu isi yaparken surekli olarak kendisini bosa
cikaran kodu kontrol eder ve bu kodun bekleme suresi bittiginde buna geri
doner (callback) ve islemi tamamlar sonra diger zipladigi kodda kaldigi yerden devam
eder. Senkron(vanilla(pure)) function buna izin vermedigi icin eventloop
dan ilk islemi beklemek bitince geri oraya atanamaz, cunku asenkron olarak
define edilmedi. Senkron islemlerde ne olursa olsun islemin bitmesi
gerekir ki sonraki line lar execute edilsin.
'''


import asyncio

# Basic usage
async def hello():
    print('Hello World')
asyncio.run(hello()) # "Hello World"


# Not proper to async example 
async def main():
    print('Alicem')
    # foo() will give error because it is async 
    await foo('text')
    print('finished')# 2-this should've been running instead
    
async def foo(text):
    print(text)
    await asyncio.sleep(1) # 1-Here we should have done sth else

asyncio.run(main())
'''
Output:
Alicem
text
finished
'''


# We should create a task to use async efficiently

async def main():
    print('Alicem')
    task = asyncio.create_task(foo('text')) # This means that save it 
    # as a coroutine task after this functions execution run this task.
    print('finished')
    
async def foo(text):
    print(text)
    await asyncio.sleep(1)

asyncio.run(main())
'''
Output:
Alicem
finished
text
'''

# But if we await the task
async def main():
    print('Alicem')
    task = asyncio.create_task(foo('text'))  
    await task # WE SHOULD WAIT UNTIL TASK FINISHES THEN NEXT LINE Thread is not idle until it finishes
    print('finished')
    
async def foo(text):
    print(text)
    await asyncio.sleep(1)

asyncio.run(main())

#await means while running if thread is idle for a moment come back execute other async works until it wants to use thread again.
# NOW
async def main():
    print('Main calismaya basladi.')
    print('Main async task okundu. Beklemeye gidiliyor.')
    task = asyncio.create_task(foo('text'))
    await asyncio.sleep(10)
    print('Main fonksiyonu sonu.')
    
async def foo(text):
    print(f'Foo fonksiyonu calisti verilen metin: {text}')
    await asyncio.sleep(1)
    task2 = asyncio.create_task(bar())
    print('Foo fonksiyonu sonu')

async def bar():
    print('Bar fonksiyonu basladi.')


asyncio.run(main())

# Main calismaya basladi
# Main async task okundu. Beklemeye gidiliyor.
# Foo fonksiyonu calisyi verilen metin text
# Foo fonksiyonu sonu
# Bar fonksiyonu basladi
# Main fonksiyonu sonu
'''
main fonksiyonunda ilk iki print statment calisti. task degiskeni async
bir degisken ve bir coroutine objesi. Hafizaya alindi. Bu fonksiyonu 
calistiran thread idle olur olmaz hafizaya alindigi icin hemen task 
calistirilacak. await ile async bekleme execute edildi ve 10 saniye thread
bosa cikti. Hemen hafizaya alinan task objesi execute edildi ve foo fonskiyonu calisti ilk print statement calisti. await ile 1 saniye bekleme
coroutine islemi execute edildi. Bu esnada thread bosa cikti ve hafizaya
alinan baska async bir komut varmi dedi ve olmadigini gorunce beklemeye 
devam etti 1 saniye boyunca ve main fonksiyonundaki 10 saniyelik bekleme 
bitmedigi icin buraya da donmedi yani callback olmadi. 1 saniyelik bekleme
bitti ve task2 execute edildi ve asenkron bir islem oldugu hafizaya atildi
await ile execute edilmedigi icin hafizada kaldi ancak fonksiyon son
satiri execute ettiginde hafizada kalan bu task2 yi calistirdi. Bu sirada
main fonksiyonundaki 10 saniyelik beklemeden geriye kalan sure oldugu icin
task2 execute ile bar fonksiyonuda calisti ve print edildi. main fonks-
iyonundan geriye kalan surenin dolmasi bitince main fonksiyonunun son
satiri execute edildi ve main fonksiyonu sonu diye ekrana yazildi
'''

#################### FETCH EXAMPLE and FUTURE OBJECT ###################
async def fetch_data():
    print('Start Fetching.')
    await asyncio.sleep(2)
    print('Done fetching.')
    return {'data':1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def main():
    task1 = asyncio.create_task(fetch_data()) # scheduled task1
    task2 = asyncio.create_task(print_numbers()) # scheduled task2
    
    value = await task1 # Future object( waiting return value==promise in js)
    print(value)
    await task2

asyncio.run(main())
'''
Output:
Start Fetching.
0
1
2
3
4
5
6
7
Done fetching.
{'data': 1}
8
9

-main icerisinde tasklar schedule edildi
-task1 den donecek data value ye assign edildi(future object)
-task1 basladi print statement calisti
-task1 await 2 saniye.
-bekleme islemi gelmisken schedule ettigim diger task2 ye geceyim 2 saniye sonra donerim
-task2 0-10 kadar numaralari 0.25 sn gecikmeli ekrana bas
0.25 * 8 inci sayi = 2 saniye doldu
-task1 e don ve devam et print statement ve return value assing et bu arada 
task2 de yarim kalan islem var ama await bitmesini bekle denilmedi simdilik devam
ediyorum.
-print(value) data ekrana basildi.
- await task2 -> fonksiyon sona ermeden task2 de yarim kalan isini bitir 8,9
ekrana basildi.
'''
