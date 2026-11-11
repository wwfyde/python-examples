import asyncio


async def main():
    print("do Something")
    await asyncio.Future()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("结束信号")
    except asyncio.CancelledError:
        print("取消")
