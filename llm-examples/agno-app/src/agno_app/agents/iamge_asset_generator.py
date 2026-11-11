"""图像素材生成"""

from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from textwrap import dedent

from openai import AsyncOpenAI, OpenAI

from lib import settings
from agno_tools.seedream import SeedDreamTools


client = OpenAI(http_client=settings.http_client)
async_client = AsyncOpenAI(http_client=settings.http_client_async)

# print(settings)
image_agent = Agent(
    # model=OpenAIChat(id="gpt-4o-mini", http_client=http_client),
    model=OpenAIResponses(id="gpt-4o-mini", async_client=async_client, client=client),
    name="image_agent",
    tools=[
        SeedDreamTools(),
        # ReasoningTools(add_instructions=True),
        # YFinanceTools(
        #     stock_price=True,
        #     analyst_recommendations=True,
        #     company_info=True,
        #     company_news=True,
        # ),
    ],
    description=dedent("""\
                    Seedream图片生成
                """),
    instructions=dedent("""\
            你是一名素材助手. 根据prompt 生成 简单的素材图案
            \
        """),
    show_tool_calls=True,
    exponential_backoff=True,  # 指数退避
    delay_between_retries=2,  # 2秒后重试
    debug_mode=True,
)


async def main():
    # image_agent.print_response(
    #     "工笔画风格，三维古风，东方禅意，航拍高角度视角，捕捉了海底极小人物的奔跑追逐；构图大面积留白和丰富的光影，背景以水墨晕染展现水中阳光的多彩折射，现实与虚拟相结合的思考，水墨风格，蓝绿色调，"
    #     "逆光和辉光效果增强冷暖对比，高角度拍摄景深感，整体画面高清，画质通透，发光呈现幽静空灵感; "
    #     "文字: “大展鸿图” 128px, 水平方向, 水平垂直居中",
    #     stream=True,
    # )
    image_agent.print_response()
    images = image_agent.get_images()
    if images and isinstance(images, list):
        for image_response in images:
            image_url = image_response.url
            print(f"Generated image URL: {image_url}")


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())

    # More example prompts to try:
    """
    Try these creative prompts:
    1. "Generate a steampunk-style robot playing a violin"
    2. "Design a peaceful zen garden during cherry blossom season"
    3. "Create an underwater city with bioluminescent buildings"
    4. "Generate a cozy cabin in a snowy forest at night"
    5. "Create a futuristic cityscape with flying cars and skyscrapers"
    """
