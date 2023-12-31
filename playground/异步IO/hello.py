import asyncio


def hello_world():
    print("hello, world!")
    for i in range(10):
        yield i
    # return 23


async def main():
    print('hello')
    for i in hello_world():
        print(i)
    await asyncio.sleep(1)
    print('world')


if __name__ == '__main__':
    asyncio.run(main())

    my_list = [chr(ord('a') + i) for i in range(1, 10, 2)]
    pass
