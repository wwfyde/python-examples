A = 1


class ClassDecorator:
    __doc__ = "docker"

    def __init__(self, func):

        # To do something before initial
        print('装饰器初始化')
        self.__func = func

    def __call__(self, *args, **kwargs):
        # 装饰器中要执行的内容
        print(f"装饰器要执行的内容")
        print(kwargs)
        # self.__func(*args, **kwargs)
        return self.__func


@ClassDecorator()
def test(b, a=1):

    print(f'被装饰的函数')


def main():
    test('b=demo', 123444)


if __name__ == '__main__':
    main()
    print(ClassDecorator.__dict__)
    ClassDecorator(func=1)(a=1)