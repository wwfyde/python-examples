import asyncio


async def task(n):
    print(f"start task {n}")
    await asyncio.sleep(1)
    print(f"end task {n}")
    return n


async def main():
    tasks = [task(i) for i in range(3)]
    print(tasks)
    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    print('main() is done')
    for d in done:
        print(await d)


if __name__ == '__main__':
    asyncio.run(main())
