import asyncio
import time
from contextlib import asynccontextmanager

@asynccontextmanager
async def timeit():
    now = time.monotonic()
    print('start')
    try:
        yield
    finally:
        print(f'it took {time.monotonic() - now}s to run')


@timeit()
async def main():
    print('hello')
    # ... async code ...
    await asyncio.sleep(1)
    print('world')

if __name__ == '__main__':
    asyncio.run(main())