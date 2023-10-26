class InvalidOperation(Exception):
    def __init__(self, message=None):
        self.message = message or 'invalid operation'


def divide(num1, num2=1):
    """
    除法
    :param num1: int
    :param num2: int
    :return: float
    """
    if num2 == 0:
        raise InvalidOperation()
    val = num1 / num2
    return val


try:
    v = divide(200, 100)
except InvalidOperation as e:
    print(e.message)
else:
    print(v)


# divide消息协议
# float divide(1: int num1, 2: int num2=1) => InvalidOperation
