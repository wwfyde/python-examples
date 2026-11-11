import json
from typing import Mapping

from orjson import orjson


def dumps(obj: Mapping) -> str:
    return orjson.dumps(obj, option=orjson.OPT_SORT_KEYS).decode()


# orjson.OPT_APPEND_NEWLINE # 增加换行
# orjson.OPT_INDENT_2 # 缩进2个空格
# orjson.OPT_NON_STR_KEYS 允许非字符串的键
def orjson_dumps(obj):
    return orjson.dumps(obj, option=orjson.OPT_SORT_KEYS).decode()


def json_dumps(obj):
    return json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":"))



if __name__ == "__main__":

    data = {
        "key3": "value1",
        "key2": "value2",
        "key1": "你好",
    }
    o = orjson_dumps(data)
    j = json_dumps(data)
    print(o)
    print(j)
    assert o == j, f"{o=}{j=}"
