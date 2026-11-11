from agents import Agent, Runner
from pydantic import BaseModel


class OutputFormat(BaseModel):
    result: str


async def start():
    triage_agent = Agent(
        name="triage",
        instructions="You are a helpful assistant",
        model="gpt-4o-mini",
        output_type=OutputFormat,
    )

    result = await Runner.run(
        triage_agent, "Write a haiku about recursion in programming."
    )
    print(result.final_output_as(OutputFormat))


if __name__ == "__main__":
    import asyncio

    asyncio.run(start())
