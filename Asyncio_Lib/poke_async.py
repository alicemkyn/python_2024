import asyncio
import aiohttp
import requests
import logging
from random import randint, seed
from time import perf_counter
from os import urandom
from typing import AsyncIterable, Iterable

# Basic settings
logging.basicConfig(level=logging.DEBUG, format='%(message)s')
lg = logging.debug
seed = urandom(1024)


# Set a constant
POKE_LIMIT = 898
url = 'https://pokeapi.co/api/v2/pokemon/{}'
entry = int(input('How many pokemon name do you want to see?\n'))


# Asynchronous Part 
async def get_pokemon(session: aiohttp.ClientSession, url: str) -> str:
    async with session.get(url.format(randint(1, POKE_LIMIT))) as request:
        response = await request.json()
        #lg(str(response['name']).capitalize())
        return str(response['name']).capitalize()


async def main(entry: int) -> AsyncIterable:
    start = perf_counter()
    async with aiohttp.ClientSession() as session:
        tasks = [get_pokemon(session, url) for _ in range(entry)]
        result = await asyncio.gather(*tasks)
        lg(result)
    lg(f'{entry} pieces of pokemon name retrieved asynchronously in {round(perf_counter() - start, 2)} seconds.')
        

# Synchronous Part
def sync_get_pokemon() -> str:
    response = requests.get(url.format(randint(1, POKE_LIMIT)))
    name = str(response.json()['name']).capitalize()
    return name


def main_sync(entry: int) -> Iterable:
    start = perf_counter()
    ls = []
    for _ in range(entry):
        ls.append(sync_get_pokemon())
    lg(ls)
    lg(f'{entry} pieces of pokemon name retrieved synchronously in {round(perf_counter() - start, 2)} seconds.')



if __name__ == '__main__':
    asyncio.run(main(entry))
    main_sync(entry)