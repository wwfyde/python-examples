import asyncio
import pika
import pika.adapters.asyncio_connection


async def main(loop):
    connection = pika.adapters.asyncio_connection.AsyncioConnection(
        pika.ConnectionParameters('localhost'),
        loop=loop,
        on_open_callback=lambda: print(" [x] Connection opened")
    )


async def on_connection_open(connection):
    print("Connection opened")
    await connection.channel(on_open_callback=on_channel_open)


async def on_channel_open(channel):
    print("Channel opened")
    # 声明队列
    queue = await channel.queue_declare(queue='hello')
    # 发送消息
    await channel.basic_publish(exchange='',
                                routing_key='hello',
                                body='Hello World!')
    print("Message sent")
    await channel.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()
