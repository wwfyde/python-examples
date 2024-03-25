"""
参考资料:
- [httpx._types](https://github.com/encode/httpx)

"""
from typing import Union, Sequence, Tuple, Mapping, TypeVar

# 自定义类 Headers Forward References
# 尚未定义的类或类型别名, 使用字符串字面量代替
HeaderTypes = Union[
    "Headers",
    Mapping[str, str],
    Mapping[bytes, bytes],
    Sequence[Tuple[str, str]],
    Sequence[Tuple[bytes, bytes]],
],

# 边界(上界), 表示T可以是<type>类型及其子类型
# T = TypeVar('T', bound='<type>')
S = TypeVar('S', bound=str)  # Can be any subtype of str
T = TypeVar('T')  # Can be anything
A = TypeVar('A', str, bytes)  # Must be exactly str or bytes
