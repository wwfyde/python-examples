from openai import OpenAI


def main():
    client = OpenAI()
    response = client.responses.create(
        model="gpt-5-nano",
        instructions="You are a professional python/rust programmer, skilled at coding and system design. response with markdown format.",
        input="如何阅读源码",
    )

    print(response.output_text)


if __name__ == "__main__":
    main()
