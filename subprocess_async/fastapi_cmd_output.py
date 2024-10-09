import asyncio
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from uvicorn import run

app = FastAPI()


async def run_command(command):
    # 启动异步子进程，并捕获 stdout
    process = await asyncio.create_subprocess_exec(
        *command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    # 迭代子进程的 stdout 输出，并以 SSE 格式发送
    try:
        async for line in process.stdout:
            yield f"data: {line.decode().strip()}\n\n"
    finally:
        # 确保进程被正确关闭
        await process.wait()


@app.get("/stream")
async def stream_logs():
    command = ["ping", "-c", "4", "google.com"]  # 使用适合你系统的命令
    return StreamingResponse(run_command(command), media_type="text/event-stream")


# 运行 FastAPI 应用
# 可以通过 `uvicorn` 或其他 ASGI 服务器运行这个应用，例如:
# uvicorn main:app --reload

if __name__ == '__main__':
    run(app, host="0.0.0.0", port=8000)
