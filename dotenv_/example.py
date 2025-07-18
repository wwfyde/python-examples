import os

from dotenv import load_dotenv, find_dotenv


def main():
    # 自动查找当前目录及父级目录的.env文件
    load_dotenv(find_dotenv())
    print(os.getenv("A", "未找到"), os.getenv("B", None))


if __name__ == "__main__":
    main()
