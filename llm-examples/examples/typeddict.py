from typing import TypedDict


class Foo(TypedDict):
    foo: str


foo: Foo = {"foo": "bar"}
foo_list: list[Foo] = [{"foo": bar} for bar in ["bar"]]
foo_dict: dict[str, Foo] = {bar: {"foo": bar} for bar in ["bar"]}
