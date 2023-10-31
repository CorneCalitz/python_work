import asyncio

async def add(x, y):
    await asyncio.sleep(3)
    return x + y

async def get_results():
    inputs = [(2,3), (4,5), (6,7), (8,2), (5,5)]

    cors = [add(x,y) for x,y in inputs]

    results = asyncio.gather(*cors) # the five coroutine objects are passed ot the event loop instance

    print(await results)

get_results()