import os

from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

load_dotenv(find_dotenv())
# client = OpenAI(api_key=os.getenv("UNIFIED_API_KEY"), base_url="https://api.ganjiuwanshi.com/v1/")
client = OpenAI(
    api_key=os.getenv("ANTHROPIC_API_KEY"),
    base_url=os.getenv("UNIFIED_API_BASE_URL", "https://api.ganjiuwanshi.com/v1/"),
)

response = client.chat.completions.create(
    model="aws-claude-3-5-sonnet-latest",
    messages=[{"role": "assistant", "content": "You are a helpful assistant"}],
    temperature=0.7,
    max_tokens=64,
    top_p=0.9,
    stream=False,
)

print(response)
