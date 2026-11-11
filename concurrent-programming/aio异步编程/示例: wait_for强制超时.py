import asyncio


async def print_interval():
    for i in range(5):
        print(f'Interval: {i}')
        await asyncio.sleep(1)


async def run_too_long():
    print('Task is running')
    task = asyncio.create_task(print_interval())
    await task
    print(f"任务完成状态: {task.done()}")
    await asyncio.sleep(12)
    print('Task is done')


async def main():
    try:
        await asyncio.wait_for(run_too_long(), timeout=8)
    except asyncio.TimeoutError:
        print('Task is not done')
    print('main() is done')


if __name__ == '__main__':
    with asyncio.Runner() as runner:
        runner.run(main())
