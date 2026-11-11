from typing import Any

from agents import Agent
from agno.models.openai import OpenAIResponses
from agno.run.response import RunResponse
from agno.workflow import Workflow
from openai import AsyncOpenAI, OpenAI

from lib import settings

client = OpenAI(http_client=settings.http_client)
async_client = AsyncOpenAI(http_client=settings.http_client_async)

class MyWorkflow(Workflow):
    description = "A workflow that do something"
    agent: Agent = Agent(
        model=OpenAIResponses(id="gpt-4o-mini", async_client=async_client, client=client),
        instructions="",
                  )


    def run(self, topic: str, use_search_cache: bool = True) -> RunResponse:
        from agno.utils.log import logger
        logger.info(f"topic is {topic}")

        