import threading
import time


def task1():
    print("task1 start")
    time.sleep(2)
    print("task1 end")


def task2():
    print("task2 start\n")
    time.sleep(4)
    print("task2 end\n ")


if __name__ == '__main__':
    start_time = time.time()
    thread1 = threading.Thread(target=task1)
    thread2 = threading.Thread(target=task2)
    # thread1.setDaemon(True)
    # thread2.setDaemon(True)

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    print("main thread end")
    print(f"time aggreate: {time.time() - start_time}")