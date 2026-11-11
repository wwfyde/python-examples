import base64
import json
import os
from enum import Enum
from mimetypes import guess_type
from pathlib import Path
from typing import Annotated, cast

from dotenv import find_dotenv, load_dotenv
from fastapi import APIRouter, Body, Depends, FastAPI, File, UploadFile
from fastapi.openapi.docs import get_swagger_ui_html
from openai import AsyncOpenAI
from openai.types.chat import ChatCompletionDeveloperMessageParam
from openai.types.chat.completion_create_params import ResponseFormat
from openai.types.responses import ResponseInputParam
from pydantic import AnyHttpUrl, BaseModel, ConfigDict
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles
from api.routes import seedream_router
from lib import settings


class Color(Enum):
    # RED = ("red", "红色")
    RED = "红"
    # GREEN = ("green", "绿色")
    GREEN = "绿"
    # BLUE = ("blue", "蓝色")
    BLUE = "蓝"
    # YELLOW = ("yellow", "黄色")
    YELLOW = "黄"
    # PINK = ("pink", "粉色")
    PINK = "粉"
    WHITE = "白"
    PURPLE = "紫"
    ORANGE = "橙"
    CYAN = "青"
    # GRAY = "灰色"
    BROWN = "棕"
    BLACK = "黑"
    # MULTICOLOR = "多色"


class ColorEn(Enum):
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
    GRAY = "gray"
    BROWN = "brown"
    BLACK = "black"
    MULTICOLOR = "multicolor"


color_map = dict(
    red="红",
    green="绿",
    blue="蓝",
    yellow="黄",
    pink="粉",
    white="白",
    purple="紫",
    orange="橙",
    cyan="青",
    gray="灰",
    black="黑",
    brown="棕",
    multicolor="多",
)


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
    objects: list[str] | None = None
    colors: list[Color | str] | None = None
    styles: list[str] | None = None
    scenes: list[str] | None = None
    foreground: Color | str = None
    background: Color | str = None
    # dominant_color: Color | str | None = None
    dominant: Color | str | None = None
    has_text: bool | None = None
    is_transparent: bool | None = None
    is_black_and_white: bool | None = None

    model_config = ConfigDict(use_enum_values=True)


class TagResponse(Tag):
    colors_en: list[str] | None = None
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "objects": ["人", "车"],
                "colors": ["红", "绿"],
                "styles": ["写实", "卡通"],
                "scenes": ["户外", "城市"],
                "foreground": "蓝",
                "background": "白",
                "dominant": "白",
                "colors_en": ["red", "green"],
            }
        },
    )


class Response(BaseModel):
    data: BaseModel | list[BaseModel] | None = None
    code: int = 200
    message: str | None = None
    elapsed_time: float | None = None
    request_id: str | None = None
    timestamp: int | None = None


PROMPT_INSTRUCTION = """
You are a professional image tagger. You need to tag the image according to the following rules:
- Identify the main objects, colors, styles, scenes, foreground color, background color and dominant color in the image and list them.
- colors items: 红, 绿, 蓝, 黄, 粉, 白, 紫, 橙, 青, 棕, 黑
- the listed colors should be ordered by the frequency of occurrence in the image to describe the primary colors,  exclude multicolor.
- the list item should be in Chinese.
- the styles represent style of art, such as 写实, 卡通, 动漫, 绘画, 素描;
- return the tag results with JSON directly without wrapping <json> tag or include any additional information.

"""
PROMPT_INSTRUCTION_QWEN = """
You are a professional image tagger. You need to tag the image according to the following rules:
- Identify the main objects, colors, styles, scenes, foreground color, background color and dominant color in the image and list them.
- let all_colors = [红, 绿, 蓝, 黄, 粉, 白, 紫, 橙, 青, 棕, 黑];
- the listed colors should be ordered by the frequency of occurrence in the image to describe the primary colors, and the value of colors must be in all_colors, at most 5 colors;
- the value of foreground, background and dominant must be in all_colors ;
- the list item should be in Chinese.
- the styles represent style of art, such as 写实, 卡通, 动漫, 绘画, 素描;
- return the tag results with JSON directly without wrapping <json> tag or include any additional information.

---Output Example---
{
  "objects": ["女孩","泰迪熊"],
  "colors": ["蓝","粉","橙","白","红"],
  "styles": ["动漫"],
  "scenes": ["艺术","肖像"],
  "foreground": "蓝",
  "background": "白",
  "dominant": "蓝",
  "has_text": false,
  "is_transparent": false,
  "is_black_and_white": false,
  "colors_en": ["blue","pink","orange","white","red"]
}
"""

router = APIRouter()

load_dotenv(find_dotenv())  # 加载环境变量


def get_openai_client():
    """
    获取openai client
    :return:
    """
    # 这里可以根据需要传入参数
    return AsyncOpenAI(
        # api_key=os.getenv("UNIFIED_API_KEY"),
        api_key=os.getenv("OPENAI_API_KEY")
        # base_url="https://api.ganjiuwanshi.com/v1/",
    )


def get_dashscope_client():
    """
    获取Qwen client
    :return:
    """
    return AsyncOpenAI(
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url=os.getenv("DASHSCOPE_BASE_URL", "https://dashscope.aliyuncs.com/compatible-mode/v1"),
    )


class ImageTag(BaseModel):
    url: AnyHttpUrl | str

    model_config = ConfigDict(
        json_schema_extra={"example": {"url": "https://wwfyde.oss-cn-hangzhou.aliyuncs.com/images/202505151425386.png"}}
    )


@router.post("/image_tag", summary="上传文件并标注", response_model=TagResponse)
async def image_tag(
    file: Annotated[UploadFile, File(description="上传位图文件(jpg,png等)")],
    client: AsyncOpenAI = Depends(get_openai_client),
):
    """
    图片标注: 识别图像主题, 颜色, 艺术风格和场景
    :return:
    """
    if not file:
        return {"message": "No file uploaded"}
    content = await file.read()
    base64_image = base64.b64encode(content).decode("utf-8")
    file_type = file.content_type
    file_type2 = guess_type(file.filename)

    url = f"data:{file_type};base64,{base64_image}"
    response = await client.responses.parse(
        model="gpt-4o",
        instructions=PROMPT_INSTRUCTION,
        input=cast(
            ResponseInputParam,
            [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_image",
                            "image_url": url,
                        },
                    ],
                }
            ],
        ),
        text_format=Tag,
    )

    tag = response.output_parsed
    tag_response = TagResponse.model_validate(tag)
    color_map_reversed = {v: k for k, v in color_map.items()}
    tag_response.colors = tag_response.colors[:3] if tag_response.colors else []
    tag_response.colors_en = [color_map_reversed.get(color, color) for color in tag.colors[:3]]
    return tag_response


@router.post("/image_tag_qwen", summary="上传文件并标注(灵积-千问)", response_model=TagResponse)
async def image_tag_qwen(
    file: Annotated[UploadFile, File(description="上传位图文件(jpg,png等)")],
    client: AsyncOpenAI = Depends(get_dashscope_client),
):
    """
    图片标注: 识别图像主题, 颜色, 艺术风格和场景
    :return:
    """
    if not file:
        return {"message": "No file uploaded"}
    content = await file.read()
    base64_image = base64.b64encode(content).decode("utf-8")
    file_type = file.content_type
    file_type2 = guess_type(file.filename)

    url = f"data:{file_type};base64,{base64_image}"
    # response = await client.responses.parse(
    #     model="gpt-4o",
    #     instructions=PROMPT_INSTRUCTION,
    #     input=cast(
    #         ResponseInputParam,
    #         [
    #             {
    #                 "role": "user",
    #                 "content": [
    #                     {
    #                         "type": "input_image",
    #                         "image_url": url,
    #                     },
    #                 ],
    #             }
    #         ],
    #     ),
    #     text_format=Tag,
    # )
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
                        {"type": "text", "text": PROMPT_INSTRUCTION_QWEN},
                        {
                            "type": "image_url",
                            "image_url": {"url": url},
                        },
                    ],
                },
            ],
        ),
        response_format=cast(ResponseFormat, {"type": "json_object"}),
    )

    result = response.choices[0].message.content
    result_obj = json.loads(result)
    # result_obj["colors"][:] = result_obj["colors"][:3]
    # result_obj["colors_en"][:] = result_obj["colors_en"][:3]
    result_model = TagResponse.model_validate(result_obj)
    result_model.colors = result_model.colors[:3] if result_model.colors else []
    return result_obj

    tag = response.output_parsed
    tag_response = TagResponse.model_validate(tag)
    color_map_reversed = {v: k for k, v in color_map.items()}
    tag_response.colors = tag_response.colors[:3] if tag_response.colors else []
    tag_response.colors_en = [color_map_reversed.get(color, color) for color in tag.colors]
    return tag_response


@router.post("/image_tag_by_url", summary="按URL标注图片", response_model=TagResponse)
async def image_tag_by_url(
    # url: Annotated[AnyHttpUrl | str, Body(description="图片url")] = None,
    params: Annotated[
        ImageTag,
        Body(
            examples=[
                {"url": "https://wwfyde.oss-cn-hangzhou.aliyuncs.com/images/202505151425386.png"},
                {"url": "https://wwfyde.oss-cn-hangzhou.aliyuncs.com/images/202505151425386.png"},
            ]
        ),
    ],
    client: AsyncOpenAI = Depends(get_dashscope_client),
):
    """
    图片标注: 识别图像主题, 颜色, 艺术风格和场景
    :return:
    """
    url = params.url
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
                        {"type": "text", "text": PROMPT_INSTRUCTION_QWEN},
                        {
                            "type": "image_url",
                            "image_url": {"url": url},
                        },
                    ],
                },
            ],
        ),
        response_format=cast(ResponseFormat, {"type": "json_object"}),
    )
    result = response.choices[0].message.content
    result_obj: dict = json.loads(result)
    result_model = TagResponse.model_validate(result_obj)
    result_model.colors = result_model.colors[:3] if result_model.colors else []
    result_model.colors_en = result_model.colors_en[:3] if result_model.colors else []
    return result_model
    result_obj["colors"][:] = result_obj["colors"][:3]
    result_obj["colors_en"][:] = result_obj["colors_en"][:3]
    return result_obj
    response = await client.responses.parse(
        model="gpt-4o",
        instructions=PROMPT_INSTRUCTION,
        input=cast(
            ResponseInputParam,
            [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_image",
                            "image_url": url,
                        },
                    ],
                }
            ],
        ),
        text_format=Tag,
    )

    tag = response.output_parsed
    tag_response = TagResponse.model_validate(tag)
    color_map_reversed = {v: k for k, v in color_map.items()}
    tag_response.colors = tag_response.colors[:3] if tag_response.colors else []
    tag_response.colors_en = [color_map_reversed.get(color, color) for color in tag.colors]

    return tag_response


@router.post("/image_tag_by_url2", summary="按URL标注图片(OpenAI)", response_model=TagResponse)
async def image_tag_by_url_openai(
    # url: Annotated[AnyHttpUrl | str, Body(description="图片url")] = None,
    params: Annotated[
        ImageTag,
        Body(
            examples=[
                {"url": "https://wwfyde.oss-cn-hangzhou.aliyuncs.com/images/202505151425386.png"},
                {"url": "https://wwfyde.oss-cn-hangzhou.aliyuncs.com/images/202505151425386.png"},
            ]
        ),
    ],
    client: AsyncOpenAI = Depends(get_openai_client),
):
    """
    图片标注: 识别图像主题, 颜色, 艺术风格和场景
    :return:
    """
    url = params.url
    response = await client.responses.parse(
        model="gpt-4o",
        instructions=PROMPT_INSTRUCTION,
        input=cast(
            ResponseInputParam,
            [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_image",
                            "image_url": url,
                        },
                    ],
                }
            ],
        ),
        text_format=Tag,
    )

    tag = response.output_parsed
    tag_response = TagResponse.model_validate(tag)
    color_map_reversed = {v: k for k, v in color_map.items()}
    tag_response.colors = tag_response.colors[:3] if tag_response.colors else []
    tag_response.colors_en = [color_map_reversed.get(color, color) for color in tag.colors[:3]] if tag.colors else []

    return tag_response


def create_app():
    """
    通过工厂函数创建app
    :return:
    """
    app = FastAPI(
        title=settings.app_name, openapi_tags=[], openapi_prefix="", openapi_url="/openapi.json", root_path="/api"
    )

    # 注册路由
    app.add_middleware(
        CORSMiddleware,
        # allow_origins=settings.CORS_ORIGINS,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    static_path = Path(__file__).parent.joinpath("static")
    app.mount("/static", StaticFiles(directory=static_path), name="static")

    @app.get("/docs2")
    async def custom_swagger_ui_html():
        return get_swagger_ui_html(
            openapi_url="/openapi.json",
            title="API Docs",
            swagger_js_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js",
            swagger_css_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css",
        )

    @app.get("/")
    async def root():
        return RedirectResponse("/docs2")

    app.include_router(router=router, prefix="/tools", tags=["tools"])
    app.include_router(router=router, prefix="/image-tools", tags=["tools"])

    return app


app = create_app()


app.include_router(seedream_router, prefix="/seedream")
