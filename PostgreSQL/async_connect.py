import asyncio
import os

import psycopg
from psycopg.rows import dict_row


async def connect_task():
    async with await psycopg.AsyncConnection.connect(os.getenv('POSTGRESQL_DSN'), row_factory=dict_row) as conn:
        async with conn.cursor(row_factory=dict_row) as cursor:
            await cursor.execute("select version()")
            version: str

            version, = await cursor.fetchone()
            print(f"Version: {version}")
            await cursor.execute("select id, name from test")

            id: int
            name: str
            id, name = await cursor.fetchone()
            print(f"id: {id}, name: {name}")


if __name__ == '__main__':
    asyncio.run(connect_task())
