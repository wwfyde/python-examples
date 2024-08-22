"""
io, 数据库, 数据结构等操作时, 避免竞态出现

"""
import asyncio

a = 2


async def op_shared_var():
    async with asyncio.Lock():
        global a
        a *= 2
        return a


async def main():
    tasks = set()
    for i in range(10):
        tasks.add(op_shared_var())

    L = await asyncio.gather(*tasks)
    print(a)
    print(L)


if __name__ == '__main__':
    asyncio.run(main())
