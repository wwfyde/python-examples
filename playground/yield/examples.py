"""
从函数中返回一个生成器(generator), 使用yield可以让函数在保持当前执行状态的情况下返回一个值给调用者, 并且在下一次从函数调用点继续执行. 这使得yield非常适合处理大数据集、实现协程、构建流式处理管道等场景，因为它可以减少内存消耗并提高程序效率。
"""


# 用法一 使得函数称为生成器函数
def gen():
    yield 1
    yield 2
    yield 3


print(type(gen()))

print(next(gen()))
print(next(gen()))
print(next(gen()))
for value in gen():
    print(value)


# 方法二 无限序列生成器
def infinite_integers():
    n = 0
    while True:
        yield n
        n += 1


gen = infinite_integers()
print(next(gen))
print(next(gen))
print(next(gen))


# 大文件读取
def read_lines(file):
    with open(file, 'r') as f:
        for line in f:
            yield line.strip()


for line in read_lines('file'):
    print(line)
