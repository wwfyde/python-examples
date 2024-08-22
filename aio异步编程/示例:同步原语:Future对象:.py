import asyncio


def on_future_done(future: asyncio.Future):
    print(future.result())


async def set_future_result(future):
    await asyncio.sleep(2)
    future.set_result("Future is done!")


async def main():
    future = asyncio.Future()
    future.add_done_callback(on_future_done)
    task = asyncio.create_task(set_future_result(future))

    # Wait until *future* has a result and print it.
    await task
    # or
    task.add_done_callback(lambda future: print(f"Callback: {future.result()}"))


if __name__ == '__main__':
    asyncio.run(main())
