import time
from agno.agent import RunResponse
from agno.utils.log import logger
from agno.utils.pprint import pprint_run_response
from agno.workflow import Workflow

from agno_agents.image_prompt_writer import prompt_agent
from agno_agents.seedream import image_agent
from agno_agents.content import content_agent
from agno_agents.content_expansion import content_expansion_agent


class CacheWorkflow(Workflow):
    # Add agents or teams as attributes on the workflow
    # agent = Agent(model=OpenAIChat(id="gpt-4o-mini", http_client=settings.http_client))
    image_agent = image_agent
    content_agent = content_agent
    content_expansion_agent = content_expansion_agent
    prompt_agent = prompt_agent

    # Write the logic in the `run()` method
    def run(self, message: str) -> RunResponse:
        # 内容生成
        content = self.content_agent.run(message)

        title = content.content.title
        outline: list[str] = content.content.outline
        outline_contents = []
        outline_figures = []

        # 文案扩写, 并生成prompt和图
        for item in outline[:2]:  # TODO: 演示模式限制2个
            item_response = self.content_expansion_agent.run(message=f"topic:{title}, sub topic: {item}")
            outline_contents.append(item_response.content)
            logger.info(f"正在生成: {item}, 文案: {item_response.content}")
            time.sleep(0.5)

            # 根据文案生成prompt
            item_prompt = self.prompt_agent.run(message=item_response.content).content
            logger.info(f"prompt --- {item}: {item_prompt}")

            # 图像生成
            image_response = self.image_agent.run(message=item_prompt)
            item_image_url = image_response.images[0] if image_response.images else None
            logger.info(item_image_url)
            outline_figures.append(item_image_url)

        # 内容聚合 合成器
        # TODO: synthesizer
        logger.info(f"Checking cache for '{message}'")
        # Check if the output is already cached
        logger.info(f"图片:{outline_figures}")
        logger.info(f"目录: {outline}")

        if self.session_state.get(message):
            logger.info(f"Cache hit for '{message}'")
            return self.image_agent.run(message)

        logger.info(f"Cache miss for '{message}'")
        # Run the agent and yield the response
        # content = self.image_agent.run(message, stream=True)
        return self.image_agent.run(message)

        # Cache the output after response is yielded
        # self.session_state[message] = self.agent.run_response.content


my_workflow = CacheWorkflow()
if __name__ == "__main__":
    response = my_workflow.run(message="雪花啤酒, 营销策划")
    # logger.info(response.content)
    pprint_run_response(response, markdown=True)
