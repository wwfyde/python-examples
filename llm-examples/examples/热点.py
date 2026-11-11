import os
import asyncio
from enum import Enum

import httpx
from dotenv import find_dotenv, load_dotenv


class SourceType(Enum):
    """来源类型, rere"""

    weixin = "微信"
    xhs = "小红书"
    weibo = "微博"
    douyin = "抖音"
    zhihu = "知乎"
    toutiao = "头条"
    baidu = "百度"
    # taobao = "淘宝"


hashid_map = {
    "weixin": "j8Rv21noLw",
    "xhs": "L4MdA5ldxD",
    "weibo": "KqndgxeLl9",
    "douyin": "K7GdaMgdQy",
    "zhihu": "rx9oz6oXbq",
    "toutiao": "WmoO5Akd4E",
    "baidu": "Jb0vmloB1G",
    # "taobao": "yjvQDpjobg",
}

all_platforms = ["微信", "小红书", "微博", "抖音", "知乎", "头条", "百度"]

nodes = [hashid_map[i.name] for i in SourceType]
print(nodes)
base_tophub_url = "https://api.tophubdata.com"
tophub_node_url = f"{base_tophub_url}/nodes"
load_dotenv(find_dotenv())
tophub_access_key = os.getenv("TOPHUB_ACCESS_KEY")

hotspot_context = {}

search_tags = ["AIGC", "人工智能", "科技", "互联网", "设计", "AI", "品牌营销"]


async def fetch_hotspot(client: httpx.AsyncClient, node: str):
    async with asyncio.Semaphore(7):
        resp = await client.get(f"{tophub_node_url}/{node}", headers={"Authorization": tophub_access_key})
        data = resp.json()
        name = data.get("data", {}).get("name", "")
        items = [
            dict(
                rank=item.get("rank", ""),
                title=item.get("title", ""),
                # description=item.get("description", ""),
                temprature=item.get("extra", ""),
            )
            for item in data.get("data", {}).get("items", [])
        ]
        return {name: items}


async def start():
    async with httpx.AsyncClient(timeout=180) as client:
        tasks = [fetch_hotspot(client, node) for node in nodes]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        for result in results:
            if isinstance(result, Exception):
                print(f"Error fetching data: {result}")
            else:
                hotspot_context.update(result)
        return hotspot_context




if __name__ == "__main__":
    result = asyncio.run(start())
    print(result)
