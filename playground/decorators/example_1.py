

def log_foo(func):
    def wrapper(*args, **kwargs):

        print(f"wrapper", *args)
        pass
    return wrapper


@log_foo
def add(a, b):
    print("func")
    return a + b


if __name__ == '__main__':
    print(add(2, 3))
