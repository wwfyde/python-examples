import base64
import os
from enum import Enum
from typing import cast

from dotenv import find_dotenv, load_dotenv
from openai import AsyncOpenAI
from openai.types.chat import ChatCompletionDeveloperMessageParam
from pydantic import BaseModel, ConfigDict


class Color(Enum):
    # RED = ("red", "红色")
    RED = "red"
    # GREEN = ("green", "绿色")
    GREEN = "green"
    # BLUE = ("blue", "蓝色")
    BLUE = "blue"
    # YELLOW = ("yellow", "黄色")
    YELLOW = "yellow"
    # PINK = ("pink", "粉色")
    PINK = "pink"
    WHITE = "white"
    PURPLE = "purple"
    ORANGE = "orange"
    TEAL = "teal"
    CYAN = "cyan"


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
    colors: list[Color]
    styles: list[str]
    scenes: list[str]

    model_config = ConfigDict(use_enum_values=True)


PROMPT_INSTRUCTION = """
You are a professional image tagger. You need to tag the image according to the following rules:
- Identify the main objects, colors, styles, scenes in the image and list them.
- return the tag results with JSON directly without wrapping <json> tag or include any additional information.

"""

# Load environment variables from .env file
load_dotenv(find_dotenv())


client = AsyncOpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=os.getenv("DASHSCOPE_BASE_URL"),
)

url = "https://wwfyde.oss-cn-hangzhou.aliyuncs.com/images/202505151425386.png"


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


async def main():
    # TODO  this not work for qwen
    # A：当前通义千问 API 支持根据您输入的提示词生成合法的 JSON 字符串，无法根据您提供的 JSON Schema 来生成。
    # https://help.aliyun.com/zh/model-studio/json-mode#7ccf14e1a1g53
    response = await client.beta.chat.completions.parse(
        model="qwen-vl-plus",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant designed to output JSON.",
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": PROMPT_INSTRUCTION},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://wwfyde.oss-cn-hangzhou.aliyuncs.com/images/202505151425386.png"
                        },
                    },
                ],
            },
        ],
        response_format=Tag,
    )

    result = response.choices[0].message.parsed
    print(result)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
