from abc import ABCMeta


# 元类用于创建或修改类, 为某一类型定制行为, 控制类的创建过程, 用于创建类的特殊类
# 默认所有类的元类都是 type, 通过定义元类可以在类创建时插入自定义逻辑
# 1.	拦截类的创建（在类生成前后自动修改或检查类）；
# 2.	自动注册类；
# 3.	自动添加或修改属性、方法；
# 4.	实现单例模式、接口检查等功能。


class MyClass(ABCMeta):
    # mcs 描述 metaclass 元类本身
    def __new__(mcs, name, bases, attrs):
        print(f"Creating class {name}")
        s = super().__new__(mcs, name, bases, attrs)
        print("Class created")
        return s


class DemoClass(metaclass=MyClass):
    def __init__(self):
        print("DemoClass instance created")

    def __new__(cls, *args, **kwargs):
        print("Creating DemoClass instance")
        instance = super().__new__(cls)
        return instance

    def method(self):
        print("Method called")


demo = DemoClass()
