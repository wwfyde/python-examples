import os

import httpx
from anthropic import AnthropicVertex

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

LOCATION = "us-east5"
# 认证 https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment?hl=zh-cn
client = AnthropicVertex(
    region=LOCATION,
    project_id="inner-virtue-462009-c5",
    # max_retries=99,
    # timeout=httpx.Timeout(1800, connect=1800, read=1800, write=1800),
    # access_token="AIzaSyAjx5mNt-uijmlAO92UeBTaabMyjJBgfGY",
)

with client.messages.stream(
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Send me a recipe for banana bread.",
        }
    ],
    model="claude-sonnet-4@20250514",
) as stream:
    for text in stream.text_stream:
        print(text)
