import asyncio
import websockets
import time

async def send_progress(websocket, message):
    await websocket.send(message)

async def main():
    # 连接到WebSocket服务器
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:

        # 步骤1
        await send_progress(websocket, "步骤1开始")
        time.sleep(1)  # 模拟操作
        await send_progress(websocket, "步骤1完成")

        # 步骤2
        await send_progress(websocket, "步骤2开始")
        time.sleep(2)  # 模拟操作
        await send_progress(websocket, "步骤2完成")

        # 步骤3
        await send_progress(websocket, "步骤3开始")
        time.sleep(1.5)  # 模拟操作
        await send_progress(websocket, "步骤3完成")

        await send_progress(websocket, "所有步骤已完成")

asyncio.get_event_loop().run_until_complete(main())