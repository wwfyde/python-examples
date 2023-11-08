class Demo:

    def __init__(self, a):
        self.a = a

    @staticmethod
    def demo():
        print("hello, 世界!")

    @classmethod
    def cls(cls):
        cls.demo()
        print(f"{__name__}, {cls.__name__}, {cls.demo()}")

    def inst(self):
        print(f"hello, 世界!@@@{self.a}")


if __name__ == '__main__':
    Demo.demo()
    Demo.cls()
    Demo.inst(self=Demo(1))
    b = Demo(12)
    b.demo()
