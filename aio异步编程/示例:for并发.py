import asyncio


async def task(i: int) -> int:
    await asyncio.sleep(1)
    return i


async def main():
    tasks = [task(i) for i in range(10)]
    results = await asyncio.gather(*tasks)
    print(results)