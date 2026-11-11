from typing import TypedDict, cast

from langgraph.graph import StateGraph
from langgraph.runtime import Runtime
from pydantic import BaseModel


class State(BaseModel):
    x: str


class Context(BaseModel):
    r: int


graph = StateGraph(state_schema=State, context_schema=Context)


def node(state: State, runtime: Runtime[Context]) -> dict | BaseModel:
    r = runtime.context.r
    x = state.x
    print(x * r)
    return {"result": x * r}


graph.add_node("A", node)
graph.set_entry_point("A")
graph.set_finish_point("A")
compiled = graph.compile()
step1 = compiled.invoke(cast(BaseModel, {"x": "你好"}), context=Context(r=3))
print(step1.values())
