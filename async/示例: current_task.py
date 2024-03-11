import asyncio


async def my_task():
    # 获取当前任务的引用
    task = asyncio.current_task()
    print(f"Current task: {task}")
    # 模拟异步操作
    await asyncio.sleep(1)
    print("Task completed")


async def main():
    # 创建并启动任务
    task = asyncio.create_task(my_task())
    # 等待任务完成
    await task


asyncio.run(main())
