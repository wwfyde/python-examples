import asyncio
import json
from typing import Annotated, TypedDict

from langchain_core.messages import BaseMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition


# 1. 定义状态
class State(TypedDict):
    # add_messages 会将新消息追加到现有列表，而不是覆盖
    messages: Annotated[list[BaseMessage], add_messages]


# 2. 模拟一个简单的工具
async def search_weather(location: str):
    """搜索指定城市的实时天气。"""
    return f"{location} 的天气晴，25°C。"


tools = [search_weather]
llm = ChatOpenAI(model="gpt-5-nano").bind_tools(tools)


# 3. 定义节点逻辑
async def call_model(state: State):
    response = await llm.ainvoke(state["messages"])
    return {"messages": [response]}


# 4. 构建图
workflow = StateGraph(State)

workflow.add_node("agent", call_model)
workflow.add_node("tools", ToolNode(tools))

workflow.add_edge(START, "agent")
workflow.add_conditional_edges("agent", tools_condition)
workflow.add_edge("tools", "agent")

app = workflow.compile()


# 5. 异步运行与日志记录
async def run_agent(query: str, log_file: str = "agent_log.jsonl"):
    inputs = {"messages": [HumanMessage(content=query)]}

    print(f"--- 开始任务: {query} ---")

    with open(log_file, "a", encoding="utf-8") as f:
        # 使用 astream_events 捕获细粒度输出 (v2 API)
        async for event in app.astream(inputs, stream_mode="values"):
            # 获取当前状态下最后一条消息
            latest_message = event["messages"][-1]

            # 构建日志条目
            log_entry = {
                "type": latest_message.type,
                "content": latest_message.content,
                "tool_calls": getattr(latest_message, "tool_calls", []),
                "name": getattr(latest_message, "name", "assistant")
            }

            # 1. 打印到控制台
            print(f"\n[{log_entry['type'].upper()}] {log_entry['name']}:")
            print(f"Content: {log_entry['content'] or '(Tool Calling...)'}")

            # 2. 写入文件 (JSONL 格式)
            f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")
            f.flush()


if __name__ == "__main__":
    asyncio.run(run_agent("告诉我上海现在的天气怎么样？"))
