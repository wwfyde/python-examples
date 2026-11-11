from openai import OpenAI

brand_tags = ["AIGC", "人工智能", "科技", "互联网", "设计", "AI", "品牌营销"]
client = OpenAI()
response = client.responses.create(
    model="gpt-5-mini",
    input="帮我获取品牌相关的热点, 关键词: " + ",".join(brand_tags),
    tools=[
        {
            "type": "web_search",
            "user_location": {
                "type": "approximate",
                "country": "CN",
                "timezone": "Asia/Shanghai",
            },
        }
    ],
    tool_choice="required",
    # reasoning={"effort": "low"},
)

brand_hotspot = response.output_text
print(brand_hotspot)
