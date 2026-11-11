from typing import Annotated

from langgraph.graph import StateGraph
from langchain_openai import ChatOpenAI
from langgraph.constants import END, START
from langgraph.graph.message import add_messages

from pydantic import BaseModel


class State(BaseModel):
    messages: Annotated[list, add_messages]


graph_builder = StateGraph(State)

# llm = init_chat_model("gpt-5-mini", model_provider="openai")
llm = ChatOpenAI(name="gpt-5-mini", temperature=0, max_retries=3, use_responses_api=True)


def chatbot(state: State) -> str:
    response = llm(state.messages)
    return {"messages": [llm.invoke(state[State])]}


graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)
graph = graph_builder.compile()

from IPython.display import Image, display

try:
    display(Image(graph.get_graph().draw_mermaid_png()))
except Exception:
    # This requires some extra dependencies and is optional
    print("Graph visualization not available")
    pass
