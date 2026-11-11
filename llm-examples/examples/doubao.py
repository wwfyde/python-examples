import os
from openai import OpenAI

from dotenv import find_dotenv, load_dotenv

# 请确保您已将 API Key 存储在环境变量 ARK_API_KEY 中
# 初始化Ark客户端，从环境变量中读取您的API Key
load_dotenv(find_dotenv())
api_key = os.environ.get("ARK_API_KEY")
print(api_key)
client = OpenAI(
    # 此为默认路径，您可根据业务所在地域进行配置
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    # 从环境变量中获取您的 API Key。此为默认方式，您可根据需要进行修改
    api_key=api_key,
)

response = client.chat.completions.create(
    # 指定您创建的方舟推理接入点 ID，此处已帮您修改为您的推理接入点 ID
    # model="doubao-1-5-thinking-vision-pro-250428",
    model="deepseek-r1-250528",
    messages=[
        {"role": "system", "content": "你是一名人工智能助手"},
        {
            "role": "user",
            "content": "你是谁？",
        },
    ],
    extra_body={"thinking": {"type": "disabled"}},
)

print(response.choices[0])
