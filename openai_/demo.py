from openai import OpenAI

client = OpenAI(

)

completion = client.chat.completions.create(
    # model="ep-20240618053250-44grk",
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
)

print(completion.choices[0].message)
print(completion.usage)
print(completion.usage.prompt_tokens)
print(completion.usage.completion_tokens)
