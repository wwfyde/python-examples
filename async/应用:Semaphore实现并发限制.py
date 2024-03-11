import asyncio

# 创建一个Semaphore，最大允许5个协程同时运行
semaphore = asyncio.Semaphore(5)


async def task(i):
    async with semaphore:
        # 模拟耗时任务
        print(f"Task {i} is running")
        await asyncio.sleep(1)
        # 任务代码...


async def main():
    # 创建并启动多个协程
    tasks = [task(i + 1) for i in range(100)]
    await asyncio.gather(*tasks)

    print("All tasks completed.")


# 运行事件循环
asyncio.run(main())
