import redis

r = redis.Redis(decode_responses=True)

r.set('a', '测试')
result = r.get('a')
print(type(result))
print(result.__doc__)
...
