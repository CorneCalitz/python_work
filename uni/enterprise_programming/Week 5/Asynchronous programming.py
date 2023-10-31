"""
Not multithreading. Uses concurrency to execute tasks. Instead of a thread being idle while waiting for task
to be completed. Rather than waiting for task, the thread is used.
Think of waiter getting orders between 2 tables. Instead of waiting for the kitchen after getting order, the waiter
takes the order of the other table.

asynchronous used?
 - When you have input and output task

Concurrency: executing parts of a program at different times
"""

import asyncio

# sync and await are keywords that go hand in hand

async def getName():
    await asyncio.sleep(5)
    return 'fred'


async def getAge():
    await asyncio.sleep(5)
    return 10


async def printInfo():
    name = await getName()
    age = await getAge()

    print(f'The name {name} and age {age}')


await printInfo()
