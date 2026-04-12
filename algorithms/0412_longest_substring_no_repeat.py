s = "abcabcbb"

def longest_substring(s:str) -> int:
    '''
    Find longest substring without repeating character in a string.

    Args:
        long_str: A string

    Returns:
        Length of substring.
    '''
    sub_str = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        if s[right] in sub_str:
            sub_str.remove(s[left])
            left += 1
        
        sub_str.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length

print(longest_substring(s))