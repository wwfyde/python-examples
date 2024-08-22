import asyncio
import time


def blocking_io(delay: int = 1, id: int = 0):
    print(f"blocking_io {id} start at {time.strftime('%X')}")
    print(f"start blocking_io at {time.strftime('%X')}")
    # Note that time.sleep() can be replaced with any blocking
    # IO-bound operation, such as file operations.
    time.sleep(delay)
    print(f"blocking_io complete at {time.strftime('%X')}")


def infinite_io():
    while True:
        time.sleep(2)
        print("infinite_io")


async def main():
    print(f"started main at {time.strftime('%X')}")

    await asyncio.gather(
        asyncio.to_thread(blocking_io, 1, 1),
        asyncio.to_thread(blocking_io, 1, 2),
        asyncio.to_thread(blocking_io, 1, 3),
        asyncio.to_thread(blocking_io, 1, 4),
        # asyncio.to_thread(infinite_io),
        asyncio.sleep(4))

    print(f"finished main at {time.strftime('%X')}")


if __name__ == '__main__':
    asyncio.run(main())
