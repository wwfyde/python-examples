from agno.playground.settings import PlaygroundSettings
from agno.playground import Playground

from agno_agents.seedream import image_agent

playground = Playground(
    agents=[image_agent],
    settings=PlaygroundSettings(
        title="agno-playground",
        cors_origin_list=["https://app.agno.com", "http://localhost:5100"],
    ),
)
# app = playground.get_app(use_async=False)
app = playground.get_app(use_async=True)

if __name__ == "__main__":
    playground.serve("playground:app", reload=True)
