import httpx
from agno.agent import Agent
from agno.models.openai import OpenAIResponses

from lib import settings
from agno_tools.hackernews import get_top_hackernews_stories


async def main():
    http_client = httpx.Client(proxy=settings.proxy_url or "http://127.0.0.1:7890")
    from textwrap import dedent

    agent = Agent(
        model=OpenAIResponses(id="gpt-4o-mini", http_client=http_client),
        tools=[get_top_hackernews_stories],
        description=dedent("""获取Hacker News"""),
        instructions=dedent("""\
            You are a tech-savvy Hacker News reporter with a passion for all things technology! 🤖
        Think of yourself as a mix between a Silicon Valley insider and a tech journalist.

        Your style guide:
        - Start with an attention-grabbing tech headline using emoji
        - Present Hacker News stories with enthusiasm and tech-forward attitude
        - Keep your responses concise but informative
        - Use tech industry references and startup lingo when appropriate
        - End with a catchy tech-themed sign-off like 'Back to the terminal!' or 'Pushing to production!'

        Remember to analyze the HN stories thoroughly while keeping the tech enthusiasm high!\
        """),
        show_tool_calls=True,
        markdown=True,
    )

    agent.print_response("Summarize the top 5 stories on hackernews?", stream=True)
    # images = image_agent.get_images()
    # if images and isinstance(images, list):
    #     for image_response in images:
    #         image_url = image_response.url
    #         print(f"Generated image URL: {image_url}")


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
    # More example prompts to try:
    """
    Try these creative prompts:
    1. "Generate a steampunk-style robot playing a violin"
    2. "Design a peaceful zen garden during cherry blossom season"
    3. "Create an underwater city with bioluminescent buildings"
    4. "Generate a cozy cabin in a snowy forest at night"
    5. "Create a futuristic cityscape with flying cars and skyscrapers"
    """
