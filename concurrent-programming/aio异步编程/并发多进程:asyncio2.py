import asyncio
from concurrent.futures import ProcessPoolExecutor
import time


# Define an I/O-bound blocking function
def io_bound_function(n):
    print(f"Starting I/O task for {n}")
    time.sleep(n)  # Simulate a blocking I/O task
    result = f"Task {n} completed"
    print(result)
    return result


# Wrap the I/O-bound function for asyncio
async def run_io_task(pool, n):
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(pool, io_bound_function, n)
    return result


# Main async function to run tasks concurrently
async def main():
    with ProcessPoolExecutor() as pool:
        tasks = [run_io_task(pool, i) for i in range(1, 6)]
        results = await asyncio.gather(*tasks)
        print(f"Results: {results}")


if __name__ == "__main__":
    asyncio.run(main())
