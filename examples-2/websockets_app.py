# gateway_server.py  –  Python 3.12
import asyncio
import json
import secrets
import time
from enum import Enum

# from websockets.server import serve, WebSocketServerProtocol
from websockets.exceptions import ConnectionClosedOK
from websockets.legacy.server import WebSocketServerProtocol, serve

HEARTBEAT_INTERVAL = 30_000  # ms


class OP(int, Enum):
    DISPATCH = (0,)
    HEARTBEAT = (1,)
    IDENTIFY = (2,)
    HELLO = (10,)
    HEARTBEAT_ACK = 11


class ClientSession:
    def __init__(self, ws: WebSocketServerProtocol):
        self.ws = ws
        self.session_id = secrets.token_hex(8)
        self.seq: int | None = None
        self.last_ack = time.monotonic()

    # ---- 发送统一入口 -------------------------------------------------------
    async def send(self, op: int, d: dict | int | None = None, t: str | None = None):
        payload = {"op": op, "d": d, "s": self.seq, "t": t}
        await self.ws.send(json.dumps(payload, separators=(",", ":")))

    # ---- 握手与心跳 ---------------------------------------------------------
    async def handshake(self) -> None:
        await self.send(OP.HELLO, {"heartbeat_interval": HEARTBEAT_INTERVAL})
        async for raw in self.ws:
            data: dict = json.loads(raw)
            match data["op"]:
                case OP.IDENTIFY:
                    # 此处仅示例校验 token，可接 DB / OAuth
                    if data["d"].get("token") != "super‑secret":
                        await self.ws.close(4003, "Not Authenticated")
                        return
                    await self.send(
                        OP["DISPATCH"], {"session_id": self.session_id}, "READY"
                    )
                    break
                case _:
                    await self.ws.close(4002, "Protocol Error")
                    return

    async def start_heartbeat_loop(self) -> None:
        while True:
            await asyncio.sleep(HEARTBEAT_INTERVAL / 1000)
            await self.send(OP["HEARTBEAT"], self.seq)
            # 如果 2 个间隔未收到 ACK → 断线
            if time.monotonic() - self.last_ack > (2 * HEARTBEAT_INTERVAL / 1000):
                await self.ws.close(4000, "Heartbeat Timeout")
                break

    # ---- 主循环 -------------------------------------------------------------
    async def run(self) -> None:
        await self.handshake()
        heartbeat_task = asyncio.create_task(self.start_heartbeat_loop())
        try:
            async for raw in self.ws:
                data: dict = json.loads(raw)
                op = data["op"]
                if op == OP["HEARTBEAT"]:
                    await self.send(OP["HEARTBEAT_ACK"])
                    self.last_ack = time.monotonic()
                elif op == OP["DISPATCH"]:
                    # 业务事件，例如聊天消息
                    ...
                else:
                    await self.ws.close(4002, "Unknown Opcode")
        except ConnectionClosedOK:
            pass
        finally:
            heartbeat_task.cancel()


async def main():
    async with serve(lambda ws: ClientSession(ws).run(), "0.0.0.0", 8765):
        print("Gateway running on ws://localhost:8765")
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
