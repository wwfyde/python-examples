import asyncio


async def run_command(command):
    # 启动异步子进程，并捕获 stdout 和 stderr
    process = await asyncio.create_subprocess_exec(
        *command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    # 迭代子进程的 stdout 输出
    async for line in process.stdout:
        print(f"STDOUT: {line.decode().strip()}")

    # 等待子进程完成，并获取返回码
    return_code = await process.wait()
    print(f"Process finished with return code: {return_code}")


# 示例使用
async def main():
    command = ["ping", "-c 4", "google.com"]  # 使用适合你系统的命令
    await run_command(command)


# 运行 asyncio 事件循环
asyncio.run(main())
