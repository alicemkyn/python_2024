import asyncio
import aiohttp
import logging
from typing import AsyncIterable
import requests
from random import randint
from time import perf_counter
'''
Stackoverflow answer:
Concurrency is two lines of customers ordering from a single cashier
(lines take turns ordering)
Parallelism is two lines of customers ordering from two cashiers
(each line gets its own cashier)
'''

logging.basicConfig(level=logging.DEBUG, format='%(message)s')
lg = logging.debug


JSON = int | str | float | bool | None | dict[str, "JSON"] | list["JSON"]
JSONObject = dict[str, JSON]
JSONList = list[JSON]


#The highest pokemon ID
MAX_POKEMON = 898 # Constant


def http_get_sync(url: str) -> JSONObject:
    response = requests.get(url)
    return response.json()


async def http_get(url: str) -> JSONObject:
    return await asyncio.to_thread(http_get_sync, url)    


async def http_get_aiohttp(url: str) -> JSONObject:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()
    

def get_random_pokemon_name_sync() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}'
    pokemon = http_get_sync(pokemon_url)
    return str(pokemon['name']).capitalize()

async def get_random_pokemon_name() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = await http_get(pokemon_url)
    return str(pokemon['name']).capitalize()


def main_sync() -> None:
    pokemon_name = get_random_pokemon_name_sync()
    print(pokemon_name)


async def next_pokemon(total: int) -> AsyncIterable[str]:
    for _ in range(total):
        name = await get_random_pokemon_name()
        yield name


async def main_generator() -> None:
    time_before = perf_counter()
    async for name in next_pokemon(20):
        print(name)
    print(f"Total time (async_gen): {perf_counter() - time_before} seconds")


async def main_for_loop() -> None:
    # We will be waiting in for loop to get pokemon_name NO ADVANTAGE of using concurrency
    time_before = perf_counter()
    for _ in range(20): 
        pokemon_name = await get_random_pokemon_name()
        print(pokemon_name)
    print(f"Total time (synchronous): {perf_counter() - time_before} seconds")


async def main_list_comprehension_on_generator() -> None:
    time_before = perf_counter()
    names = [name async for name in next_pokemon(20)]
    print(names)
    print(f"Total time (async_gen_ls_compr): {perf_counter() - time_before} seconds")
    

async def main_gather():
    time_before = perf_counter()
    result = await asyncio.gather(*[get_random_pokemon_name() for _ in range(20)])
    print(result)
    print(f"Total time (asynchronous): {perf_counter() - time_before} seconds")




if __name__ == "__main__":
    asyncio.run(main_for_loop()) #12.439647457999854 seconds
    asyncio.run(main_gather())  #0.9791616670008807 seconds
    asyncio.run(main_generator()) #12.021545333000176 seconds
    asyncio.run(main_list_comprehension_on_generator()) #12.0463760409984 seconds
    # main_sync()