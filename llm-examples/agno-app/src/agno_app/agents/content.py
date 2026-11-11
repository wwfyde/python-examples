from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from openai import AsyncOpenAI, OpenAI
from pydantic import BaseModel

from lib import settings


class ContentItems(BaseModel):
    title: str
    outline: list[str]


client = OpenAI(http_client=settings.http_client)
async_client = AsyncOpenAI(http_client=settings.http_client_async)

content_agent = Agent(
    model=OpenAIResponses(
        id="gpt-4o-mini",
        client=client,
        async_client=async_client,
    ),
    name="内容助手",
    instructions="""
    你是一名内容策划写作高手, 根据用户描述的需求内容主题目录和标题 每个主题不超过20字. 需要生成 主标题title 多个块outline
    """,
    response_model=ContentItems,
)
if __name__ == "__main__":
    response = content_agent.run("雪花啤酒, 营销海报")
    print(response.content)
