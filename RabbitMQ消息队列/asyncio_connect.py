import asyncio

import aio_pika


async def main() -> None:
    connection = await aio_pika.connect_robust(
        "amqp://MjphbXFwLWNuLTV5ZDNmdWlldzAwNTpMVEFJNXRKZXRydHlBRHYxWjRKcjVMNEE=:RUI1M0ZDMjhCMjdGQjExRTQ2M0QxQzY0QTlFOTJGQTczNDM1NDcxMzoxNjk3NTIzOTMwMzI0@amqp-cn-5yd3fuiew005.cn-hangzhou.amqp-4.net.mq.amqp.aliyuncs.com:5672/molook-uat?name=104-midjourney",
    )
    print(connection.connected)

    async with connection:
        routing_key = "test_queue"

        channel = await connection.channel()
        exchange = await channel.declare_exchange('molook', durable=True, type=aio_pika.ExchangeType.TOPIC)
        await exchange.publish(
            aio_pika.Message(body=f"Hello {routing_key}".encode()),
            routing_key=routing_key,
        )


if __name__ == "__main__":
    asyncio.run(main())
