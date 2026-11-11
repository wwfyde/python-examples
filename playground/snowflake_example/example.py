"""
可以创建一个snowflake_id 生成服务, 每个节点使用自己的id 来生成

保证时间同步和相同的位分配策略
https://discord.com/developers/docs/reference#snowflakes

"""

from snowflake import Snowflake, SnowflakeGenerator

s = Snowflake(0, 0)
# print(s())

s = SnowflakeGenerator(999)
print(next(s))
