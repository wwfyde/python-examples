from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from openai import AsyncOpenAI, OpenAI
from pydantic import BaseModel

from lib import settings


client = OpenAI(http_client=settings.http_client)
async_client = AsyncOpenAI(http_client=settings.http_client_async)

prompt_agent = Agent(
    model=OpenAIResponses(
        id="gpt-4o-mini",
        client=client,
        async_client=async_client,
    ),
    name="image prompt助手",
    instructions="""
    你是一名生图prompt creative writer, 根据文案, 为文案生成配图prompt, 生图时请紧扣主题. 
    首先理解用户的意图和核心诉求
    主题描述词, 场景, 
    美学
    专业, 
    检测是否有生成文字需求, 待生成的文字用引号包裹, 
    """,
)
if __name__ == "__main__":
    response = prompt_agent.run("""陈晓华是一位在交互体验设计领域具有重要影响力的人物。他是AiMark公司的CEO，并曾担任阿里巴巴菜鸟网络的设计总监。他在中国服务设计领域被评选为“十大杰出青年”，体现了他在行业内的卓越成就和贡献。

在他的职业生涯中，陈晓华致力于推动设计与技术的深度结合，特别关注人工智能（AI）对用户体验的影响。在2024UXGO交互体验设计大会上，他以《AI时代下的体验思考》为主题进行了演讲，分享了关于AI在设计中的应用案例，例如AI Pin和Adobe等，深入探讨了AI技术带来的机遇与挑战。他的见解为在AI时代的体验设计从业者提供了宝贵的思考方向及指导原则，强调了在技术进步背景下，体验设计的重要性和未来发展潜力。
""")
    print(response.content)
