from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from openai import AsyncOpenAI, OpenAI
from pydantic import BaseModel

from lib import settings


client = OpenAI(http_client=settings.http_client)
async_client = AsyncOpenAI(http_client=settings.http_client_async)

content_expansion_agent = Agent(
    model=OpenAIResponses(
        id="gpt-4o-mini",
        client=client,
        async_client=async_client,
    ),
    name="内容扩写助手",
    instructions="""
    你是一名内容创意扩写专家, 扩写文案长度不超过200字
    """,
)
if __name__ == "__main__":
    context = """2024年10月20日，2024UXGO交互体验设计大会在浙江省科协科学咖啡馆盛大召开。本次大会以 “交互体验设计发展新周期” 为主题，共同探讨了交互体验设计在新周期的发展方向与机遇。

AiMark CEO、阿里巴巴菜鸟网络原设计总监、中国服务设计十大杰出青年 陈晓华发表了《AI时代下的体验思考》主题演讲。通过分享AI Pin、adobe等案例，既展示了其中蕴含的巨大机遇，也提醒我们要清醒地认识到所面临的挑战，为体验设计从业者在 AI 时代的发展提供重要的思考方向和指导原则。"""
    topic = "陈晓华是谁"
    response = content_expansion_agent.run(f"<context>{context}</context>, <topic>{topic}<topic>")
    print(response.content)
