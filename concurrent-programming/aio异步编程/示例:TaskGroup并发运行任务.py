import asyncio
import time


async def saf_after(delay, what):
    while True:
        await asyncio.sleep(delay)
        print(what)
        return what
    # return what


async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(
            saf_after(1, 'hello')
        )
        task2 = tg.create_task(
            saf_after(3, 'world')
        )
        task1.add_done_callback(lambda fut: print(f"task1 done: {fut.result()}"))
        task2.add_done_callback(lambda fut: print(f"task1 done: {fut.result()}"))
        print(f"started at {time.strftime('%X')}")

    print(f"finished at {time.strftime('%X')}")
    print(task1.result(), task2.result())
    print(task1.done(), task2.done())


asyncio.run(main())
