from io import BytesIO

import requests
from PIL import Image
from pathlib import Path

file_path = "//b3fbf1a7-fe19-41b3-b640-0b4db8c5e356.png"
file_path = "/Users/wwfyde/Downloads/c43cdf31-7b1e-433c-9b45-84b94be7a13f.heic"
file_path = Path("/Users/wwfyde/Downloads") / "未命名项目-图层 1.png"

file_path = "/Users/wwfyde/projects/MoLook/Resources/image/mask.jpg"
image = Image.open(file_path)
print(image.format.lower())

url = "https://dms-upload.oss-cn-hangzhou.aliyuncs.com/seedream/b3fbf1a7-fe19-41b3-b640-0b4db8c5e356.png"
response = requests.get(url)
print(response.status_code)
image_bytes = response.content
pil = Image.open(BytesIO(image_bytes))
img_format = pil.format.lower()
print(img_format)
