import base64
import json
import os
from typing import cast

from dotenv import find_dotenv, load_dotenv
from openai import AsyncOpenAI
from openai.types.chat import ChatCompletionDeveloperMessageParam
from openai.types.chat.completion_create_params import ResponseFormat

PROMPT_INSTRUCTION = """
You are a professional image tagger. You need to tag the image according to the following rules:
- Identify the main objects, colors, styles, scenes in the image and list them.
- return the tag results with JSON directly without wrapping <json> tag or include any additional information.
---Output Example---
{
    "objects": ["cat", "dog"],
    "colors": ["red", "blue"],
    "styles": ["realistic", "cartoon"],
    "scenes": ["park", "beach"]
}
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
    response = await client.chat.completions.create(
        model="qwen-vl-plus",
        messages=cast(
            ChatCompletionDeveloperMessageParam,
            [
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
        ),
        response_format=cast(ResponseFormat, {"type": "json_object"}),
    )

    result = response.choices[0].message.content
    result_obj = json.loads(result)
    print(result)
    print(result_obj)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
