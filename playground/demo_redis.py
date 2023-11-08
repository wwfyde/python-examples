import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

if __name__ == '__main__':

    try:
        r.set("name", "吴方圆")
    except Exception as exc:
        print(exc)
        pass
    print(r.get("name"))
