# 请求Query，按照接口文档中填入即可
import io
import json
import base64
from datetime import datetime
from urllib.parse import urlencode

import httpx
import requests
from PIL import Image

from lib import settings
from lib.src.lib.volcengine import Params, create_volc_header

query_params = {
    "Action": "CVProcess",
    "Version": "2022-08-31",
}

# 请求Body，按照接口文档中填入即可
body = {
    "req_key": "jimeng_high_aes_general_v21_L",
    "prompt": "工笔画风格，三维古风，东方禅意，航拍高角度视角，捕捉了海底极小人物的奔跑追逐；构图大面积留白和丰富的光影，背景以水墨晕染展现水中阳光的多彩折射，现实与虚拟相结合的思考，水墨风格，蓝绿色调，逆光和辉光效果增强冷暖对比，高角度拍摄景深感，整体画面高清，画质通透，发光呈现幽静空灵感",
    "use_sr": True,
    "width": 768,
    "height": 768,
    "return_url": False,
    # ......
}
params = Params(
    access_key=settings.solutions.jimeng.access_key,
    secret_key=settings.solutions.jimeng.secret_key,
    body=body,
    method="POST",
    base_url=settings.solutions.jimeng.base_url,
    query_params=query_params,
    region="cn-north-1",
    service="cv",
)
# https://visual.volcengineapi.com?Action=CVProcess&Version=2022-08-31
# url = str(httpx.URL(params.base_url, params=query_params))
query_string = urlencode(sorted(params.query_params.items()))
url = params.base_url + "?" + query_string
print(url)

headers = create_volc_header(params)
# 'HMAC-SHA256 Credential=AKLTOWRkYjJmZjU1MTA4NDkwMGJhY2NhNmNjZTEyZjMzN2U/20250528/cn-north-1/cv/request, SignedHeaders=content-type;host;x-content-sha256;x-date, Signature=5aa22626cf47967a1e9e2552d1d8e28f6420251c6102f9f643734f228d906685'
response = requests.post(url, data=json.dumps(body), headers=headers)
# response = httpx.post(url, data=json.dumps(body), headers=headers, timeout=60)
# response = httpx.post(url, json=body, headers=headers, timeout=60)

print(response.status_code)
data = response.json()
if body.get("return_url", False) and data.get("data", {}).get("image_url", ""):
    image_url = data.get("data", {}).get("image_url", "")
    print(f"Image URL: {image_url}")
    image = Image.open(io.BytesIO(httpx.get(image_url).content))
    image.save(f"output_image-{datetime.now().strftime('%Y%m%d%H%M%S')}.png")  # 保存图片
else:
    image_base64 = next(iter(data.get("data", {}).get("binary_data_base64", [])), "")
    image_bytes = base64.b64decode(image_base64)
    with open("output_image2.png", "wb") as f:
        f.write(image_bytes)
    image = Image.open(io.BytesIO(image_bytes))
    image.show()  # 显示图片
