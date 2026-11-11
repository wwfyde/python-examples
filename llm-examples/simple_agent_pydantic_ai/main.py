from pydantic_ai import Agent
from pydantic_ai.providers.openai import OpenAIProvider

model = OpenAIProvider(base_url="")
agent = Agent(model="openai:gpt-4o-mini", instructions="You are a helpful assistant")
