import os

from dotenv import find_dotenv, load_dotenv
from tavily import TavilyClient

# Step 1. Instantiating your TavilyClient
load_dotenv(find_dotenv())
api_key = os.getenv("TAVILY_API_KEY")
tavily_client = TavilyClient(api_key=api_key)

brand_tags = ["AIGC", "人工智能", "科技", "互联网", "设计", "AI", "品牌营销"]

# Step 2. Executing a simple search query
response = tavily_client.search(
    "帮我获取品牌相关的热点, 关键词: " + ",".join(brand_tags), country="china", time_range="month"
)

# Step 3. That's it! You've done a Tavily Search!
print(response)
