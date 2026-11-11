import asyncio
import time


class RateLimiter:
    """"
    example:
        rate_limiter = RateLimiter(capacity=1, rate=0.2, refill_time=0.1)
        for _ in range(10):
            await rate_limiter.wait()
            # do something
    """
    def __init__(self, capacity: int, rate: float, refill_time: float = 0.1):
        # 设置桶容量
        self.capacity = capacity
        self.tokens = capacity  # 持有tokens

        # 速率限制
        self.rate = rate  # 单位时间能够添加的令牌数
        self.refill_time = refill_time  # 检查速率
        self.last_refill_time = time.time()  # 最后一次检查时间

    def add_tokens(self):
        now = time.time()
        elapsed_time = now - self.last_refill_time
        # 超过一定时间后, 添加一个令牌
        self.tokens += elapsed_time * self.rate
        self.last_refill_time = now

        # 向令牌中添加令牌, 但不能操过容量
        self.tokens = min(self.capacity, self.tokens)
        # 重置检查时间

    async def wait(self, tokens: int = 1):
        while True:
            self.add_tokens()
            # 如果桶中有足够的令牌, 则减去令牌
            if self.tokens >= tokens:
                self.tokens -= tokens
                break
            await asyncio.sleep(self.refill_time)


async def main():
    rate_limiter = RateLimiter(capacity=1, rate=0.2, refill_time=0.1)

    for _ in range(10):
        await rate_limiter.wait()
        print("Request processed")


if __name__ == '__main__':
    asyncio.run(main())
