s = "abcabcbb"

def length_of_longest_substring(s: str) -> int:
    """
    Return the length of the longest substring without repeating characters.

    Uses a sliding window approach with two pointers:
    - Expand the window with the right pointer.
    - Shrink the window from the left when duplicates are found.

    Args:
        s (str): Input string.

    Returns:
        int: Length of the longest substring without duplicate characters.
    """
    left = 0
    max_len = 0
    seen = set()

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


            

