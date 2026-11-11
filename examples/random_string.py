import random
import string


def random_string(length: int = 16, charset: str = string.ascii_letters + string.digits) -> str:
    return "".join(random.choices(charset, k=length))


if __name__ == "__main__":
    print("默认随机字符串:", random_string())
    print("纯字母(8位):", random_string(8, string.ascii_letters))
    print("纯数字(6位):", random_string(6, string.digits))
    print("含特殊字符(20位):", random_string(20, string.printable.strip()))