import os

from dotenv import load_dotenv, dotenv_values, find_dotenv


def main():
    config = {
        # **os.environ,
        **dotenv_values(),
    }
    print(config)
    print(type(config))

    # 自动查找当前目录及父级目录的.env文件
    load_dotenv(find_dotenv())

    print(os.getenv("PGUSER"), os.getenv("PGPASS"))


if __name__ == "__main__":
    main()
