import asyncio


async def infinite_task():
    while True:
        await asyncio.sleep(2)
        print("infinite_task")
        future = asyncio.Future()

        future.set_result("result")


async def main():
    task = asyncio.create_task(infinite_task())
    print("main coroutine started")
    await asyncio.sleep(6)

    await asyncio.sleep(2)

    task.cancel()  # Cancel the infinite_task
    try:
        print("explicitly call task")
        # 显式判断任务是否还在执行
        await task  # Wait until the infinite_task is cancelled
    except asyncio.CancelledError:
        print("main coroutine was cancelled")
    print("main coroutine ended")


if __name__ == '__main__':
    asyncio.run(main())
