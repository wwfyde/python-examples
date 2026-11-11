import asyncio
import time
from uuid import uuid4

import httpx

base_url = "http://127.0.0.1:9004"
endpoint = "/sdapi/v1/txt2img"
endpoint_img = "/sdapi/v1/img2img"


async def run(sem: asyncio.Semaphore, start_time: float):
    async with sem:
        async with httpx.AsyncClient(timeout=60.0 * 5) as client:
            url = base_url + endpoint
            print(url)
            route_cookie = str(uuid4())
            cookies = {"route": route_cookie}
            payload = {"prompt": "1 girl", "negative_prompt": ""}
            headers = {"Content-Type": "application/json"}
            resp = await client.post(url, json=payload, headers=headers, cookies=cookies)
            resp.raise_for_status()
            single_request_time = time.perf_counter() - start_time
            print(round(single_request_time))
            return round(single_request_time)


async def main():
    max_concurrency = 1

    start_time = time.perf_counter()
    sem = asyncio.Semaphore(7)
    tasks = [asyncio.create_task(run(sem, start_time)) for i in range(max_concurrency)]
    results = await asyncio.gather(*tasks)
    total_time = time.perf_counter() - start_time
    print(f"任务详情, {results}")
    average_time = sum(results) / len(results) if results else 0
    print(f"平均时间, {round(average_time)}")
    print(f"总时间, {round(total_time)}")


if __name__ == "__main__":
    asyncio.run(main())
