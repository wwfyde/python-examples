import asyncio


async def main():
    print("Hello...")
    await asyncio.sleep(1)
    print("...world!")

if __name__ == '__main__':
    asyncio.run(main())
