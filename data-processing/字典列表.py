dict_list = [{"a": 1, "b": 2}, {"a": 3, "b": 4}, {"a": 1, "b": 5}, {"a": 2, "b": 6}]

item = next((i for i in dict_list if i["a"] == 1), None)
item2 = next((i["a"] for i in dict_list if i["a"] == 1), None)


config_dict = {1: {"b": 2}, 2: {"b": 4}, 3: {"b": 5}, 4: {"b": 6}}
item = config_dict.get(1, {})
item2 = config_dict.get(1, {}).get("b", None)

print(item)  # Output: {'a': 1, 'b': 2}
print(item2)
