def is_valid(s:str) -> bool:
    """
    Check if a string of brackets is valid.
    A string is valid if:
    1. Every opening bracket has a corresponding closing bracket of the same type.
    2. Brackets are closed in the correct order.
    Args:
        s (str): Input string containing only '(', ')', '{', '}', '[' and ']'.
    Returns:
        bool: True if the string is valid, False otherwise.
    """
# s = {[]})
    stack: list[str] = []
    mapping = {
        ')':'(',
        ']':'[',
        '}':'{'
    }
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else "#"  
                                    # 这里#是sentinel value（哨兵值/占位值）
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return len(stack) == 0  # 检查是否匹配都完成，没完成len!==0，返回false

