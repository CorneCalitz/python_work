"""Async programming keywords
    -coroutine
    -task
    -event  loop
"""
import tracemalloc
tracemalloc.start()

import asyncio

async def add(x, y):
    await asyncio.sleep(3)
    return x + y

# thread -> coroutine object -> event loop executes your coroutine object -> handles result back to the thread

asyncio.run(add(3, 4))

print("Bye")