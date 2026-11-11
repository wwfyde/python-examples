from openai import OpenAI

client = OpenAI()
response = client.responses.create(
    model="gpt-4.1-nano",
    input="今年欧冠冠军是谁, 决赛比分如何?",
)

print(response.output_text)
