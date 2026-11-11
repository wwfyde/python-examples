import json
import base64
from uuid import uuid4
from pydantic import Field, BaseModel
from urllib.parse import urlencode

import requests
from fastapi import APIRouter

from lib import settings
from lib.src.lib.image import upload_image
from lib.src.lib.volcengine import Params, create_volc_header

router = APIRouter()


class RequestBody(BaseModel):
    """
    文档说明: https://www.volcengine.com/docs/85128/1526761#4e552e07
    接口日期: 2025-06-10
    """

    req_key: str | None = Field(
        ...,
        title="算法名称",
        description="算法名称，取固定值为high_aes_general_v30l_zt2i",
        examples=["high_aes_general_v30l_zt2i"],
    )
    prompt: str = Field(
        ...,
        title="提示词",
        description="用于生成图像的提示词 ，中英文均可输入",
    )
    use_pre_llm: bool | None = Field(
        True,
        title="是否开启文本扩写",
        description="开启文本扩写，会针对输入prompt进行扩写优化，如果输入prompt较短建议开启，如果输入prompt较长建议关闭, 默认值：false",
    )
    seed: int | None = Field(-1, title="随机种子")
    scale: float | None = Field(2.5, le=10, ge=1, title="影响文本描述的程度")
    width: int | None = Field(default=1328, ge=512, le=2048)
    height: int | None = Field(default=1328, ge=512, le=2048)
    return_url: bool | None = Field(
        None,
        title="是否返回图片链接",
        description="输出是否返回图片链接 （链接有效期为24小时）",
    )
    logo_info: dict | None = Field(None, title="水印信息")


class Prompt(BaseModel):
    prompt: str
    seed: int | None = Field(-1, title="随机种子")
    width: int | None = Field(default=1328, ge=512, le=2048)
    height: int | None = Field(default=1328, ge=512, le=2048)


@router.post("/txt2img")
async def txt2img(params: Prompt):
    access_key = settings.solutions.jimeng.access_key
    secret_key = settings.solutions.jimeng.secret_key
    if not access_key or not secret_key:
        return "Please set the `access_key` and `secret_key` for JimengTools."

    body_pydantic = RequestBody(
        req_key="high_aes_general_v30l_zt2i",
        prompt=params.prompt,
    )
    if params.width > 2048:
        params.width = 2048
    if params.height > 2048:
        params.height = 2048
    if params.seed:
        body_pydantic.seed = params.seed
    body = body_pydantic.model_dump(exclude_unset=True, exclude_none=True)
    params = Params(
        access_key=access_key,
        secret_key=secret_key,
        body=body,
    )
    query_string = (
        urlencode(sorted(params.query_params.items())) if isinstance(params.query_params, dict) else params.query_params
    )
    url = params.base_url + "?" + query_string
    headers = create_volc_header(params)
    response = requests.post(url=url, data=json.dumps(body), headers=headers)
    data = response.json()
    images_base64 = data.get("data", {}).get("binary_data_base64", [])

    response_str = ""
    urls = []
    for image_base64 in images_base64:
        if not image_base64:
            continue
        # Decode the base64 image bytes
        # Create an ImageArtifact from the decoded bytes
        image_bytes = base64.b64decode(image_base64)
        id = str(uuid4())
        filename = f"{id}.png"

        url = upload_image(filename, image_bytes, prefix="jimeng")
        urls.append(url)

    return urls
