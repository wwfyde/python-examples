from datetime import datetime


def iso_str_now(exclude_microseconds: bool = True) -> str:
    """
    获取当前时间的 ISO 格式字符串
    :param exclude_microseconds: 是否排除毫秒
    :return: ISO 格式字符串
    """
    if exclude_microseconds:
        # return datetime.now().astimezone().replace(microsecond=0).strftime("%Y-%m-%dT%H:%M:%S%z")
        # return datetime.now().astimezone().replace(microsecond=0).isoformat()
        # return datetime.now().astimezone().isoformat(timespec='seconds')
        return datetime.now().isoformat(timespec='seconds')

    return datetime.now().isoformat()


if __name__ == '__main__':
    print(iso_str_now())