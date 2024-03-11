from aiohttp import web
import asyncio


async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == web.WSMsgType.PING:
            await ws.pong()
        elif msg.type == web.WSMsgType.TEXT:
            await ws.send_str(msg.data + "/server")
        elif msg.type == web.WSMsgType.ERROR:
            print(f'ws connection closed with exception {ws.exception()}')

    print('websocket connection closed')

    return ws


app = web.Application()
app.add_routes([web.get('/ws', websocket_handler)])

if __name__ == '__main__':
    web.run_app(app)
