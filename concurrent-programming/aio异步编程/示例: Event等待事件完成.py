import asyncio
import random


async def wait_event():
    some_event = asyncio.Event()

    await asyncio.sleep(3)
    a = random.randint(1, 100)
    if a % 2 == 0:
        some_event.set()  # 标记任务完成
    else:
        pass
    try:
        await asyncio.wait_for(some_event.wait(), timeout=4)
        print("执行任务成功")

    except TimeoutError as exc:
        print(f"执行任务超时, {exc=}")


if __name__ == "__main__":
    asyncio.run(wait_event())
