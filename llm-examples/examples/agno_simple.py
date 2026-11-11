from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.run.response import RunResponse
from agno.tools.reasoning import ReasoningTools
# from agno.tools.yfinance import YFinanceTools

agent = Agent(
    model=OpenAIResponses(id="gpt-4.1-mini"),
    # tools=[
    #     ReasoningTools(add_instructions=True),
    #     YFinanceTools(
    #         stock_price=True,
    #         analyst_recommendations=True,
    #         company_info=True,
    #         company_news=True,
    #     ),
    # ],
    # instructions="Use tables to display data.",
    markdown=True,
)

run: RunResponse = agent.run("What is visual design?")

print(run.content)

var = agent.run_response.metrics
print(var)
