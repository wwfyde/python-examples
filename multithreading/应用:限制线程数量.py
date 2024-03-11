import threading
import time

semaphore = threading.Semaphore(5)


def task(i):
    with semaphore:
        print(f"Task {i} is running")
        time.sleep(1)


if __name__ == '__main__':
    threads = [threading.Thread(target=task, args=(i,)) for i in range(100)]
    for t in threads:
        t.start()
    # 保证线程都执行完毕
    for t in threads:
        t.join()
    print("All tasks completed.")
