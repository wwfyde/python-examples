import os
import threading
import time


def demo(args):
    print(f"Hello Thread {args}")


if __name__ == '__main__':
    a = 5
    m = {}
    print(dir())
    for i in range(a):
        t = threading.Thread(target=demo, args=[i])
        m[f"a_{i}"] = t

        t.start()
        time.sleep(1)

    for key, value in m.items():
        value.join()
        print(key)

