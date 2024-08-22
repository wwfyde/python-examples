"""
如果需要从非异步的部分（比如同步代码或另一个线程）安排异步任务执行，
可以使用asyncio.run_coroutine_threadsafe。
这个函数将协程加入到事件循环中，并立即返回一个concurrent.futures.Future对象。
这种方式适用于从异步代码之外的地方（如其他线程）启动异步任务。
"""
import asyncio
import threading

"""
loop = asyncio.new_event_loop()
t = threading.Thread(target=start_background_loop, args=(loop,))
t.start()

# 在后台事件循环中安排永久循环任务
asyncio.run_coroutine_threadsafe(eternal_loop(), loop)
"""


async def coro_func():
    return await asyncio.sleep(1, 42)


def in_thread(loop):
    # Later in another OS thread:
    future = asyncio.run_coroutine_threadsafe(coro_func(), loop)
    # Wait for the result:
    result = future.result()
    print(result)


def main():
    loop = asyncio.new_event_loop()
    t = threading.Thread(target=in_thread, args=(loop,))
    t.start()
    loop.run_forever()


if __name__ == '__main__':
    main()
