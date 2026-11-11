import pika
from pika.adapters.asyncio_connection import AsyncioConnection


async def consume():
    parameters = pika.ConnectionParameters('localhost')
    connection = AsyncioConnection(parameters)
    channel = connection.create_connection()
