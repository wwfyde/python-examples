"""
https://superfastpython.com/asyncio-run_coroutine_threadsafe/#Example_of_Running_a_Coroutine_From_Another_Thread
"""

import asyncio
import threading
from concurrent.futures import ThreadPoolExecutor


# 定义一个简单的异步协程函数
async def my_coroutine():
    print("Running coroutine in another thread...")

    return await asyncio.sleep(2, 12)


# 在主线程中定义一个函数，用于在另一个线程中运行协程并获取结果
def run_coroutine_in_thread(loop):
    # 使用新创建的事件循环运行协程
    future = asyncio.run_coroutine_threadsafe(my_coroutine(), loop)

    # 在主线程中等待获取协程的结果
    result = future.result()
    print("Result obtained in the main thread:", result)


async def main():
    loop = asyncio.get_running_loop()
    t = threading.Thread(target=run_coroutine_in_thread, args=(loop,))
    t.start()
    await my_coroutine()
    print('main thread')


if __name__ == '__main__':
    asyncio.run(main())
