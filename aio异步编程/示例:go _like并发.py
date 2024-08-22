import asyncio


async def my_task():
    await asyncio.sleep(1)
    print("Task done")
    return "the result"


async def main():
    task = asyncio.create_task(my_task())
    task.add_done_callback(lambda future: print(f"Callback: {future.result()}"))
    print("Task created")
    return await task


if __name__ == '__main__':
    result = asyncio.run(main())
    print(result)
