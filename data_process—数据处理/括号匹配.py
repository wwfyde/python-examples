def is_valid(s: str) -> bool:
    stack = []  # 使用栈存储左括号
    mapping = {")": "(", "]": "[", "}": "{"}
    for char in s:
        if char in mapping:  # 遇到右括号
            top_element = stack.pop() if stack else "#"
            if mapping[char] != top_element:
                return False
        else:  # 遇到左括号
            stack.append(char)
    return not stack


if __name__ == "__main__":
    assert is_valid("()()") is True
    assert is_valid("())") is False
    assert is_valid("([])") is True
    assert is_valid("([})") is False
    assert is_valid("(())") is True
