import time
from contextlib import contextmanager


@contextmanager
def timeit():
    now = time.monotonic()
    try:
        yield
    finally:
        print(f'Elapsed time: {time.monotonic() - now}')


@timeit()
def test():
    time.sleep(2)
    print()


if __name__ == '__main__':
    test()