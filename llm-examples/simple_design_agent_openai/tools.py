from agents import function_tool


@function_tool
def known_me(some: str) -> str:
    return f"{some} is known to me."
