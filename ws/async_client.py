import asyncio

import websockets.client


async def main():
    async with websockets.client.connect('ws://localhost:8765') as websocket:
        while True:
            try:
                await websocket.send("hello")
                message = await websocket.recv()
                print(message)

            except Exception as exc:
                raise exc


if __name__ == '__main__':
    asyncio.run(main())
