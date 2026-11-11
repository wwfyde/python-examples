from typing import Annotated, Literal

from langchain_core.messages import AnyMessage
from pydantic import BaseModel

from langgraph.graph import END, MessagesState, add_messages
from langgraph.types import Command
from langchain.chat_models import init_chat_model
from langchain_core.language_models.chat_models import BaseChatModel


class State(BaseModel):
    messages: Annotated[list[AnyMessage], add_messages]
    next: str


def make_supervisor_node(llm: BaseChatModel, members: list[str]) -> str:
    options = ["FINISH"] + members
    system_prompt = (
        "You are a supervisor tasked with managing a conversation between the"
        f" following workers: {members}. Given the following user request,"
        " respond with the worker to act next. Each worker will perform a"
        " task and respond with their results and status. When finished,"
        " respond with FINISH."
    )

    class Router(BaseModel):
        """Worker to route to next. If no workers needed, route to FINISH."""

        next: Literal[*options]

    def supervisor_node(state: State) -> Command[Literal[*members, "__end__"]]:
        """An LLM-based router."""
        messages = [
            {"role": "system", "content": system_prompt},
        ] + state["messages"]
        response = llm.with_structured_output(Router).invoke(messages)
        goto = response["next"]
        if goto == "FINISH":
            goto = END

        return Command(goto=goto, update={"next": goto})

    return supervisor_node


def main():
    model = init_chat_model("openai:gpt-4.1-mini")

    print("Hello from multi-agent-langgraph!")


if __name__ == "__main__":
    main()
