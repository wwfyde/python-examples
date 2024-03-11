"""

"""
import asyncio
import time


async def saf_after(delay, what):
    print(f"saf_after started at {time.strftime('%X')}")
    # 注意 当前任务的引用不应该被等待
    task = asyncio.current_task()
    print(f"task: {task}")

    while True:
        await asyncio.sleep(delay)
        print(what)
        return what


async def main():
    # 如果直接await Task对象，则不是并发执行, 而是串行执行
    task1 = asyncio.create_task(saf_after(1, 'hello'))  # Create a task to  event loop and immediately run
    task2 = asyncio.create_task(saf_after(3, 'world'))
    print(len(asyncio.all_tasks()))
    print(asyncio.all_tasks())
    await asyncio.sleep(5)
    print(f"started at {time.strftime('%X')}")

    # 该代码的作用是等待task1和task2都执行完毕后再执行下面的代码
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
