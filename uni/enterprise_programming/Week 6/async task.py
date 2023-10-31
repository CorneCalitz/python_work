import asyncio
import tracemalloc
tracemalloc.start()

async def multiply(x, y):
    await asyncio.sleep(3)
    return x * y

async def main():
    task = asyncio.create_task(multiply(3, 4))

    await task

    print(task.done())
    print(task.cancelled())

main()