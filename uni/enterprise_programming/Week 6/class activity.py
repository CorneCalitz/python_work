import asyncio

async def add(x, y):
    await asyncio.sleep(3)

    return x + y


async def substraction(x, y):
    await asyncio.sleep(3)

    return x - y


async def multiply(x, y):
    await asyncio.sleep(3)

    return x * y


async def get_results(x, y):
    cors = [add(x, y), substraction(x, y), multiply(x, y)]

    results = asyncio.gather(*cors)

    print(await results)


asyncio.run(get_results(9, 6))