import asyncio
import json
from pprint import pprint
from typing import Annotated, TypedDict

from langchain_core.messages import BaseMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import START, StateGraph
from langgraph.graph.message import add_messages


# 1. 定义状态
class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


# 2. 初始化模型 (开启 stream_usage 以确保流式输出中包含总计)
llm = ChatOpenAI(
    model="gpt-5-nano",
    temperature=0,

    # model_kwargs={"stream_options": {"include_usage": True}}
)


async def call_model(state: State):
    # 异步调用 LLM
    response = await llm.ainvoke(state["messages"])
    return {"messages": [response]}


# 3. 构建图
workflow = StateGraph(State)
workflow.add_node("agent", call_model)
workflow.add_edge(START, "agent")
app = workflow.compile()


# 4. 异步运行并提取元数据
async def run_agent_with_metrics(query: str, log_file: str = "metrics_log_messages.jsonl"):
    inputs = {"messages": [HumanMessage(content=query)]}

    print(f"--- 正在处理查询: {query} ---\n")

    with open(log_file, "a", encoding="utf-8") as f:
        # 使用 stream_mode="values" 获取每个节点生成的完整消息对象
        async for event in app.astream(inputs, stream_mode="messages"):
            pprint(event)
            print("---")
            continue
            message = event["messages"][-1]
            # print(message)

            # 提取元数据和用量
            # 现代 LangChain 消息对象包含 usage_metadata (包含 total, input, output tokens)
            usage = getattr(message, "usage_metadata", {})
            # 提取 API 响应中的底层元数据 (如 model_name, finish_reason)
            response_metadata = getattr(message, "response_metadata", {})

            output_data = {
                "role": message.type,
                "content": message.content,
                "token_usage": usage,
                "model_info": {
                    "model": response_metadata.get("model_name"),
                    "system_fingerprint": response_metadata.get("system_fingerprint"),
                    "finish_reason": response_metadata.get("finish_reason")
                }
            }

            # 打印到控制台 (增加可读性)
            if usage:
                print(f"📈 [Token Usage] Total: {usage.get('total_tokens')} "
                      f"(In: {usage.get('input_tokens')}, Out: {usage.get('output_tokens')})")

            if output_data['content']:
                print(f"🤖 [Response]: {output_data['content']}\n")

            # 写入文件
            f.write(json.dumps(output_data, ensure_ascii=False) + "\n")
            f.flush()


if __name__ == "__main__":
    asyncio.run(run_agent_with_metrics("1+1=?"))
