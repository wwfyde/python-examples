import asyncio

import redis.asyncio as redis


async def get_redis_connection_pool():
    pool = redis.ConnectionPool(db=0)
    r = await redis.Redis(connection_pool=pool, decode_responses=True)
    return r


async def get_redis_connection():
    pool = redis.ConnectionPool(decode_responses=True, protocol=3)
    r = await redis.Redis(connection_pool=pool, decode_responses=True)
    return r


async def main():
    r = await get_redis_connection()
    async with r:
        await r.set('dev_servers', '32')
        result = await r.get('a', )
        print(type(result))
        print(result.__doc__)
        await r.get(13)
        print(r.__doc__)
        # print(r.connection.db)

    r = redis.Redis(decode_responses=True)
    result = await r.get('a')
    print()


if __name__ == '__main__':
    asyncio.run(main())
