import asyncio
import random
import time


async def producer(queue: asyncio.Queue, n):
    for i in range(1, n + 1):
        await asyncio.sleep(random.randint(1, 3))  # Simulate I/O operation
        item = f'item {i}'
        await queue.put(item)
        print(f'Produced {item}')


async def consumer(queue: asyncio.Queue):
    while True:
        item = await queue.get()
        await asyncio.sleep(random.randint(1, 3))  # Simulate I/O operation
        print(f'Consumed {item}')
        queue.task_done()


async def main():
    queue = asyncio.Queue()

    # Set up the number of items to produce
    num_items_to_produce = 10

    # Launch producer and consumer tasks
    producers = [asyncio.create_task(producer(queue, num_items_to_produce))]
    consumers = [asyncio.create_task(consumer(queue)) for _ in range(2)]  # 2 consumers

    # Wait for all items to be produced
    await asyncio.gather(*producers)

    # Wait until the queue is fully processed
    await queue.join()

    # Cancel the consumers, which are now idle
    for c in consumers:
        c.cancel()


# Run the main function
asyncio.run(main())
