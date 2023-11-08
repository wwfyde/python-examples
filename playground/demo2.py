class Demo():
    def __init__(self, b):
        self.a = 12
        self.b = b
    @property
    def c(self):
        return self.a + self.b
    def __getattr__(self, item):
        return 124

    # def __getattribute__(self, item):
    #     print(f"查找到属性: {item}")



if __name__ == '__main__':
    b = Demo(23)
    # b.c = 33
    # print(b.a, b.c)
    a = []
    a.append(1)
    print(b.d)
