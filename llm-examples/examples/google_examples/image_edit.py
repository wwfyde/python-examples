from io import BytesIO
from uuid import uuid4
from pathlib import Path

import requests
from PIL import Image
from google import genai

from lib.src.lib.image import upload_image

client = genai.Client()

prompt = ("Create a picture of my cat eating a nano-banana in a fancy restaurant under the Gemini constellation",)
prompt = "一款以猫为主题的二次元贴纸，足够简介, 黑色线条为主, 不需要阴影。背景必须是透明的。 "

image_path = Path(__file__).parent.parent.parent / "data" / "my_cat.jpeg"
assert image_path.exists(), f"Image not found: {image_path}"
image = Image.open(image_path)  # File
image = "https://dms-upload.oss-cn-hangzhou.aliyuncs.com/jimeng/325347fc-994f-4493-9c76-e6415c674d3b.png"
image_bytes = BytesIO(requests.get(image).content)
image = Image.open(image_bytes)

response = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    contents=[prompt],
    # contents=[prompt, image],
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        format = part.inline_data.mime_type.split("/")[-1]
        print(f"Image format: {format}")

        url = upload_image(f"{str(uuid4())}.{format}", part.inline_data.data)
        print(url)
