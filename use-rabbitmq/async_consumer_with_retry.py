import asyncio

import aio_pika
from aio_pika import Message

MAX_RETIES = 5


async def process_message(
        message: aio_pika.abc.AbstractIncomingMessage,
) -> None:
    print(message)

    retries = int(message.headers.get('x-retries', 0))
    async with message.process(requeue=False, ignore_processed=True):
        print(message.body)
        if retries >= MAX_RETIES:
            print("超过最大重试次数")
            await message.ack()
        else:
            # retries_times = message.headers['x-retries'] = retries + 1
            new_headers = dict(message.headers)
            retry_times = new_headers['x-retries'] = retries + 1
            print(f"第{retry_times}次重试")
            new_message = Message(
                body=message.body,
                message_id=message.message_id,
                headers=new_headers
            )
            await asyncio.sleep(3)
            # channel: aio_pika.abc.AbstractRobustChannel =
            # TODO  get exchange object

            exchange = await channel.declare_exchange(
            await exchange.publish(
                message=new_message,
                routing_key=message.routing_key
            )
            # await message.nack(requeue=True)
            pass

async def republish_message(message: aio_pika.abc.AbstractIncomingMessage):

async def main() -> None:
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@127.0.0.1/",
    )

    queue_name = "molook"

    # Creating channel
    channel = await connection.channel()

    # Maximum message count which will be processing at the same time.
    await channel.set_qos(prefetch_count=1)

    # Declaring queue
    queue = await channel.declare_queue(queue_name, auto_delete=True)
    await queue.consume(process_message)

    try:
        # Wait until terminate
        await asyncio.Future()
    finally:
        await connection.close()


if __name__ == "__main__":
    asyncio.run(main())
