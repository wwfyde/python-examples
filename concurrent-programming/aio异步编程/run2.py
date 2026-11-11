import asyncio
import time


async def saf_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")
    await saf_after(1, 'hello')
    await saf_after(3, 'world')
    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
