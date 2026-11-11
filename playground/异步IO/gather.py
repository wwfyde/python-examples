"""
并发执行任务
"""

import asyncio


async def task(name, times):
    print(f'start {name}')
    for i in range(times):
        await asyncio.sleep(1)
        print(f'{name}: {i} 次')


async def main():
    print('hello')
    await asyncio.gather(task('A', 3), task('B', 4), task('C', 5))
    print('world')

asyncio.run(main())
