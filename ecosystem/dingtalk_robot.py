"""
消息
https://open.dingtalk.com/document/orgapp/message-types-and-data-format

"""
import time
import hmac
import hashlib
import base64
import urllib.parse
import httpx
from typing import Any


class DingTalkAlert:
    def __init__(self, access_token: str, secret: str):
        self.url = "https://oapi.dingtalk.com/robot/send"
        self.access_token = access_token
        self.secret = secret

    def _generate_signature(self) -> tuple[int, str]:
        """生成钉钉安全设置所需的签名"""
        timestamp = int(round(time.time() * 1000))
        secret_enc = self.secret.encode('utf-8')
        string_to_sign = f'{timestamp}\n{self.secret}'
        string_to_sign_enc = string_to_sign.encode('utf-8')

        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        return timestamp, sign

    def send_markdown(self, title: str, text: str) -> dict[str, Any]:
        """发送 Markdown 格式消息（推荐用于异常告警）"""
        timestamp, sign = self._generate_signature()
        params = {
            "access_token": self.access_token,
            "timestamp": timestamp,
            "sign": sign
        }

        payload = {
            "msgtype": "markdown",
            "markdown": {
                "title": title,
                "text": text
            },
            "at": {
                "isAtAll": False
            }
        }

        with httpx.Client(timeout=10.0) as client:
            response = client.post(self.url, params=params, json=payload)
            response.raise_for_status()
            return response.json()


# 使用示例
if __name__ == "__main__":
    # 替换为你的 Webhook 配置
    ACCESS_TOKEN = "2dba848576379e7252fe79825eabfbed2a04cd2f068a0a1177c329e3f2887ac5"
    SECRET = "SEC427e973d747db228729e5de59be18c7e8e228faef50da87ebeaaa4c5f2edeecf"

    alert = DingTalkAlert(ACCESS_TOKEN, SECRET)

    try:
        # 模拟服务异常
        1 / 0
    except Exception as e:
        error_msg = f"### 🚨 服务异常通知\n\n" \
                    f"**环境**: 生产环境\n\n" \
                    f"**错误类型**: `{type(e).__name__}`\n\n" \
                    f"**详情**: {str(e)}"

        result = alert.send_markdown("服务异常", error_msg)
        print(result)
