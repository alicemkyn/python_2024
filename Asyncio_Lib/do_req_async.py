import asyncio
import aiohttp
from time import perf_counter
import logging

# Basic settings
logging.basicConfig(level=logging.DEBUG, format='%(message)s')
lg = logging.debug

url = 'https://httpbin.org/post'
data = {
    'name':'Toru Kurosawa',
    'game':'Last Bronx',
    'weapon': 'Wooden Sword',
    'place' : 'Radical Parking Lot'
}

counter = 0
start = perf_counter()
seconds = int(input('Set the time for requests:\n'))


async def do_request(session,seconds):
    while True:
        async with session.post(url=url, data=data) as request:
            #response = await request.json()
            #lg(response['headers']['X-Amzn-Trace-Id'])
            response = await request.text()
            lg(response)
            global counter
            counter += 1
            
            if time:=round(perf_counter() - start) >= seconds:
                lg(f'Requests were posted {counter} times in {time} {round(perf_counter() - start)} seconds')
                break
                

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [do_request(session, seconds) for _ in range(50)]
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
