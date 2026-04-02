def is_valid(s:str) -> bool:
    dict_str = {
        ']':'[',
        '}':'{',
        ')':'('
    }

    stack = []
    for char in s:
        if char in dict_str.values():
            stack.append(char)
        else:
            if not stack or stack[-1] != dict_str[char]:
                return False
            stack.pop()
    return len(stack) == 0

print(is_valid("()"))      # True
print(is_valid("()[]{}"))  # True
print(is_valid("(]"))      # False
print(is_valid("([)]"))    # False
print(is_valid("{[]}"))    # True