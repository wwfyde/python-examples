import asyncio

import aio_pika


async def main() -> None:
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@127.0.0.1/",
    )

    async with connection:
        routing_key = "molook"

        channel = await connection.channel()

        # exchange = await channel.declare_exchange('molook', durable=True, type=aio_pika.ExchangeType.TOPIC)
        body = f"Hello {routing_key}".encode()
        await channel.default_exchange.publish(
            aio_pika.Message(body=body),
            routing_key=routing_key,
        )
        print(body)


if __name__ == "__main__":
    asyncio.run(main())
