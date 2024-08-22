# Define a CPU-bound or I/O-bound blocking function
import asyncio
import time
from concurrent.futures import ProcessPoolExecutor


def blocking_function(n):
    print(f"Starting computation for {n}")
    time.sleep(n)  # Simulate a long-running task
    result = n * n
    print(f"Completed computation for {n}: {result}")
    return result


# Wrap the blocking function to be used with asyncio
async def run_blocking_function(pool, n):
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(pool, blocking_function, n)
    return result


# Main asynchronous function to manage concurrency
async def main():
    time_start = time.perf_counter()
    max_workers = 3
    with ProcessPoolExecutor(max_workers=max_workers) as pool:
        tasks = [run_blocking_function(pool, i) for i in range(1, 7)]
        results = await asyncio.gather(*tasks)
        print(f"Results: {results}")
    time_end = time.perf_counter()
    print(f"Time taken: {time_end - time_start:.2f} seconds")


# Run the event loop
if __name__ == "__main__":
    asyncio.run(main())
