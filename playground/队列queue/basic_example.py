"""
生产者与消费者1:3
"""
import time
from queue import Queue

queue = Queue(10)


def producer():
    for i in range(100):
        queue.put(i)
        print(f"Produced {i}")
        time.sleep(1)


def consumer():
    while True:
        item = queue.get()
        print(f"Consumed {item}")
        queue.task_done()
        time.sleep(11)


if __name__ == '__main__':
    import threading

    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)
    producer_thread.start()
    consumer_thread.start()
    # wait until all item finished
    producer_thread.join()
    consumer_thread.join()
    print("All done")
