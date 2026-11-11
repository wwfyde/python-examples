# TODO jinja 内容合成

from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from jinja2 import Environment, StrictUndefined, Template
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
    name="内容聚合",
    instructions="""
    
    """,
    markdown=True,
)


def markdown_render(*, title, sections, contents, images):
    template = """
# {{ title }}

{# zip 过滤器将多个列表一并遍历 #}
{% for sub, text, img in sections|zip(contents, images) %}
## {{ sub }}

{{ text }}

{% if img %}
![{{ sub }}]({{ img }})
{% endif %}

{% endfor %}
    """
    env = Environment(
        autoescape=False,  # 输出 Markdown，无 HTML 转义
        undefined=StrictUndefined,  # 严格模式：引用未定义变量时报错
    )
    env.filters["zip"] = zip

    tpl = env.from_string(template)
    s = tpl.render(title=title, sections=sections, images=images, contents=contents or sections)
    print(s)
    return s
    # response = content_agent.run("")

    # print(response.content)
