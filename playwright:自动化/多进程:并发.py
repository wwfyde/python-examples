import asyncio
import os
from concurrent.futures import ProcessPoolExecutor


async def worker(i):
    print(f"task {i}")
    await asyncio.sleep(3)
    return f"task {i}"


def run(i):
    return asyncio.run(worker(i))


async def main():
    loop = asyncio.get_event_loop()
    num_processes = os.cpu_count()
    with ProcessPoolExecutor(max_workers=num_processes) as pool:
        tasks = [loop.run_in_executor(pool, run, i) for i in range(12)]

        results = await asyncio.gather(*tasks)
    print(results)


if __name__ == "__main__":
    asyncio.run(main())
