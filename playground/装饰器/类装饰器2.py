class ClassDecorator:

    def __init__(self, func):
        print('__init__ class wrapper')
        self.func = func

    def __call__(self, *args, **kwargs):
        print('when run class wrapper')
        result = self.func(*args, **kwargs)
        print('after run class wrapper')
        return result


@ClassDecorator
def tests():
    print('run target func')


if __name__ == '__main__':
    tests()
