from contextlib import contextmanager


@contextmanager
def do_something():
    a = 12
    try:
        yield a
    finally:
        del a
        print('end the context')


# do 是 yield 返回的对象
with do_something() as do:
    print(do)
