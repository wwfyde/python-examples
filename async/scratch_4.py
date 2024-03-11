import asyncio


async def task(name, seconds):
    print(f'Task {name} started')
    await asyncio.sleep(seconds)
    print(f'Task {name} completed')


async def main():
    # 创建并启动三个任务
    asyncio.create_task(task("A", 1))
    asyncio.create_task(task("B", 1))
    asyncio.create_task(task("C", 1))
    print('开始并发')
    # 等待一段时间，确保所有任务都能运行
    await asyncio.sleep(5)


asyncio.run(main())
