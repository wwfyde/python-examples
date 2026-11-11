import tempfile
from pathlib import Path

import httpx
from PIL import Image


def main():
    """从网络下载图片并写入暂存文件, 方便以路径的方式操作"""
    image_url = "https://dms-upload.oss-cn-hangzhou.aliyuncs.com/seedream/b3736283-44b7-414d-acf0-6920a877942d.jpeg"
    suffix = Path(httpx.URL(image_url).path).suffix
    response = httpx.get(image_url)
    content = response.content

    with tempfile.NamedTemporaryFile(delete=True, suffix=suffix) as tmp:
        tmp.write(content)
        filename = tmp.name
        is_exist = Path(tmp.name).exists()
        image = Image.open(filename)
        image.show()

    is_exist = Path(filename).exists()
    pass


if __name__ == "__main__":
    main()
