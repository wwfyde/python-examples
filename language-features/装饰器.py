def simple(func):  #
    def wrapper(*args, **kwargs):
        func()
        pass

    return wrapper  # 执行
