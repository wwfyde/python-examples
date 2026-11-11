from functools import lru_cache


@lru_cache
def say_hi(name: str, salutation: str = "Ms."):
    return f"Hello {salutation} {name}"


if __name__ == "__main__":
    print(say_hi("Alice"))
    print(say_hi("Bob", salutation="Dr."))
    print(say_hi("Alice"))  # This call will use the cached result
    print(say_hi("Alice"))  # This call will use the cached result
