import asyncio


def compare_version(version1: str, version2: str) -> bool:
    """
    Compare two versions.

    :param version1: First version.
    :param version2: Second version.
    :return: True if version1 is greater than version2, False otherwise.
    """
    # Split the versions into major, minor and patch numbers
    # and convert them to integers
    # version1_numbers = [int(x) for x in version1.split('.')]
    # version2_numbers = [int(x) for x in version2.split('.')]
    v1 = list(map(int, version1.split('.')))
    v2 = list(map(int, version2.split('.')))

    # 版本号项数对齐
    # while len(v1) < len(v2):
    #     v1.append(0)
    # while len(v2) < len(v1):
    #     v2.append(0)
    if len(v1) > len(v2):
        v2.extend([0] * (len(v2) - len(v1)))
    else:
        v1.extend([0] * (len(v1) - len(v2)))

    # 比较版本号项
    for i in range(len(v1)):
        if v1[i] > v2[i]:
            return True
        elif v1[i] < v2[i]:
            return False


async def example():
    await asyncio.sleep(1)  # 等待1秒
    return "Done"


async def test():
    print("never scheduled")


async def main():
    result = await example()
    print(result)
    await test()


if __name__ == '__main__':
    asyncio.run(main())
    range()
