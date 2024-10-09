import asyncio
import os
import sys

from utils.tenacity_examples import function
import redis.asyncio as redis
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


async def main():
    # print(os.environ['REDIS__PASSWORD'])
    # password = os.environ['REDIS__PASSWORD']
    redis_dsn = f"redis://:{os.environ['REDIS__PASSWORD']}@{os.environ['REDIS__HOST']}:{os.environ['REDIS__PORT']}/{os.environ['REDIS__DB']}"
    pool = redis.ConnectionPool.from_url(redis_dsn, decode_responses=True, protocol=3)
    redis_client = redis.Redis(connection_pool=pool)
    async with redis_client:
        result = await redis_client.get('a')
        return result
        # print(result)


if __name__ == '__main__':
    result = asyncio.run(main())
    print(result)
    print(sys.path)
    asyncio.run(function())
