import operator
from typing import Annotated
from pydantic import BaseModel

from langgraph.graph import StateGraph, add_messages
from langchain.agents import create_agent
from langgraph.constants import START
from langchain_core.messages import AnyMessage


class State(BaseModel):
    nlist: Annotated[list[str], operator.add]
    messages: Annotated[list[AnyMessage], add_messages]


def node_a(state: State):
    return state


# build Graph
builder = StateGraph(State)

# Add Nodes
builder.add_node("a", node_a)


# Add Edges
builder.add_edge(START, "a")

create_agent()
