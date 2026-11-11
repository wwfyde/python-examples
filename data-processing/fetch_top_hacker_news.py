import asyncio
from concurrent.futures.thread import ThreadPoolExecutor
from pprint import pprint

import httpx
from httpx import AsyncClient

TOP_STORIES_ENDPOINT = "https://hacker-news.firebaseio.com/v0/topstories.json"


def fetch_top_news(numbers: int = 10):
    t_resp = httpx.get(url=TOP_STORIES_ENDPOINT)
    t_resp.raise_for_status()
    top_story_ids = t_resp.json()[:numbers]

    # 并发
    def worker(id: int) -> dict:
        print(f"fetching: {id}")
        story_endpoint = f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
        s_resp = httpx.get(story_endpoint)
        s_resp.raise_for_status()
        story = s_resp.json()
        story_filtered = {
            key: value for key, value in story.items() if key in ["id", "title", "url"]
        }
        return story_filtered

    with ThreadPoolExecutor(max_workers=8) as executor:
        results = executor.map(worker, top_story_ids)
        stories = []

        for result in results:
            stories.append(result)

    return stories


async def fetch(client: AsyncClient, id: int) -> dict:
    print(f"fetching: {id}")
    story_endpoint = f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
    s_resp = await client.get(story_endpoint)
    s_resp.raise_for_status()
    story = s_resp.json()
    story_filtered = {
        key: value for key, value in story.items() if key in ["id", "title", "url"]
    }
    return story_filtered


async def run(num: int = 10):
    t_resp = httpx.get(url=TOP_STORIES_ENDPOINT)
    t_resp.raise_for_status()
    top_story_ids = t_resp.json()[:num]
    async with AsyncClient() as client:
        tasks = [fetch(client, id) for id in top_story_ids]
        results = await asyncio.gather(*tasks)
        stories = []
        for result in results:
            stories.append(result)

        return stories


if __name__ == "__main__":
    # pprint(fetch_top_news(10))
    pprint(asyncio.run(run(10)))
