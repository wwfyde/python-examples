def scope_test():
    def do_local():
        spam = 'local spam'
        print('In do_local:', spam)

    def do_nonlocal():
        nonlocal spam
        # 此处将修改outer scope变量
        spam = 'nonlocal spam'

    def do_global():
        global spam
        spam = 'global spam'

    spam = 'test spam'
    do_local()
    print('After local assignment:', spam)
    do_nonlocal()
    print('After nonlocal assignment:', spam)


if __name__ == '__main__':
    scope_test()
    # print('In global scope:', spam)
