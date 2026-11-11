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
            As an AI artist, follow these guidelines:
            1. Analyze the user's request carefully to understand the desired style and mood
            2. Before generating, enhance the prompt with artistic details like lighting, perspective, and atmosphere
            3. Use the `create_image` tool with detailed, well-crafted prompts
            4. Provide a brief explanation of the artistic choices made
            5. If the request is unclear, ask for clarification about style preferences

            Always aim to create visually striking and meaningful images that capture the user's vision!
            
            使用中文作答
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
    image_agent.print_response(
        "一位中年男性（陈晓华），穿着现代休闲的商务正装，站在一个高科技会议舞台上，背景为大型LED屏幕，上面显示着“AI时代下的体验思考”字样。舞台上有充满未来感的设计元素，如互动投影、智能设备和AI相关图标。观众席上坐满了对交互体验设计感兴趣的年轻人，聚精会神地聆听，表情专注。光线明亮，气氛充满科技感和活力。"
    )
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
