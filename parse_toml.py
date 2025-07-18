import tomllib


def parse_toml_file(file_path):
    """
    解析 toml 文件
    :param file_path:
    :return:
    """
    with open(file_path, "rb") as f:
        data = tomllib.load(f)
    return data


data = parse_toml_file("pyproject.toml")
print(data)
