import asyncio
import random

from tenacity import AsyncRetrying, RetryError, stop_after_attempt


async def function():
    try:
        async for attempt in AsyncRetrying(stop=stop_after_attempt(3)):
            with attempt:
                print("attempt")
                a = random.randint(0, 10)
                if a % 2 == 0:
                    print('get a even number')
                    return
                else:
                    print("the value of a is not even number ")
                    raise Exception('My code is failing!')
    except RetryError:
        print('retry error')
        pass


if __name__ == '__main__':
    asyncio.run(function())
