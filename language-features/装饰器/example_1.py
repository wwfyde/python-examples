from typing import Callable


def log_foo(n) -> Callable:  # 让装饰器 携带参数
    def decorator(
        func: Callable[[str, str], str],
    ) -> Callable:  # 装饰器函数本身, 装饰器必定是以函数为参数
        def wrapper(*args, **kwargs):
            print(f"{wrapper}", *args)
            s = func(*args, **kwargs)  # 执行被装饰的函数
            print(s)
            return s

        return wrapper

    return decorator


@log_foo(12)
def add(a, b):
    print("func")
    return a + b


add = log_foo(1)(add)

add(2 + 3)


if __name__ == "__main__":
    print(add(2, 3))
    pass
