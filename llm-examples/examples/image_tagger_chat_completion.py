import base64
from enum import Enum

from openai import AsyncOpenAI
from pydantic import BaseModel


class Color(Enum):
    RED = ("red", "红色")
    GREEN = ("green", "绿色")
    BLUE = ("blue", "蓝色")


class Object(Enum):
    PERSON = ("person", "人")
    CAR = ("car", "车")
    DOG = ("dog", "狗")
    CAT = ("cat", "猫")
    BIRD = ("bird", "鸟")
    TREE = ("tree", "树")
    HOUSE = ("house", "房子")
    FLOWER = ("flower", "花")
    SUN = ("sun", "太阳")
    MOON = ("moon", "月亮")


class Style(Enum):
    REALISTIC = ("realistic", "写实")
    CARTOON = ("cartoon", "卡通")
    ANIME = ("anime", "动漫")
    PAINTING = ("painting", "绘画")
    SKETCH = ("sketch", "素描")
    VECTOR = ("vector", "矢量")
    _3D = ("3d", "三维")
    FLAT = ("flat", "扁平化")
    LINEART = ("lineart", "线条艺术")
    LOWPOLY = ("lowpoly", "低多边形")


class Scene(Enum):
    OUTDOOR = ("outdoor", "户外")
    INDOOR = ("indoor", "室内")
    CITY = ("city", "城市")
    NATURE = ("nature", "自然")
    SPACE = ("space", "太空")
    UNDERWATER = ("underwater", "水下")
    FANTASY = ("fantasy", "幻想")
    SCI_FI = ("sci-fi", "科幻")
    HISTORICAL = ("historical", "历史")
    FUTURISTIC = ("futuristic", "未来")


class Tag(BaseModel):
    objects: list[str]
    colors: list[str]
    styles: list[str]
    scenes: list[str]


PROMPT_INSTRUCTION = """
You are a professional image tagger. You need to tag the image according to the following rules:
1. Identify the main objects in the image and list them.
"""


client = AsyncOpenAI()

url = "https://wwfyde.oss-cn-hangzhou.aliyuncs.com/images/202505151425386.png"


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


async def main():
    response = await client.chat.completions.create(
        model="gpt-4o",

        message=[
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": PROMPT_INSTRUCTION},
                    {
                        "type": "input_image",
                        "image_url": "https://wwfyde.oss-cn-hangzhou.aliyuncs.com/images/202505151425386.png",
                    },
                ],
            }
        ],
    )

    result = response.output_parsed
    print(result)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
