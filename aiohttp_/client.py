import aiohttp
import asyncio


async def heartbeat(ws):
    while True:
        print('心跳保活')
        await ws.ping()
        await asyncio.sleep(10)  # 每10秒发送一次心跳


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect('http://localhost:8080/ws') as ws:
            print('create heartbeat')
            asyncio.create_task(heartbeat(ws))  # 创建心跳任务
            print("not blocked")
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.PONG:
                    print("Pong received")
                elif msg.type == aiohttp.WSMsgType.TEXT:
                    print(f"Message received: {msg.data}")
                elif msg.type == aiohttp.WSMsgType.CLOSED:
                    break
                elif msg.type == aiohttp.WSMsgType.ERROR:
                    break


asyncio.run(main())
