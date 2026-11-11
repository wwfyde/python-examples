from pydantic import BaseModel

from IPython.display import Image, display
from langgraph.graph import StateGraph
from langgraph.constants import END, START


class State(BaseModel):
    nlist: list[str]


def node_a(state: State) -> State:
    note = "Hello"
    state.nlist.append(note)
    return state


# build a graph

builder = StateGraph(State)
builder.add_node("a", node_a)
builder.add_edge(START, "a")
builder.add_edge("a", END)


# compile to graph
graph = builder.compile()

print(graph.get_graph().draw_mermaid())
display(Image(graph.get_graph().draw_mermaid_png()))
initial_state = State(nlist=["How are you?"])
result = graph.invoke(initial_state)
print(result)

# map_reduce

# super steps
