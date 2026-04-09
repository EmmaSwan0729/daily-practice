long_str = 'abcabcbb'

def longest_sustring(long_str: str) -> int:
    '''
    Find longest substring without duplicated character in a string.

    Args:
        long_str: A string

    Returns:
        Length of substring.
    '''
    
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(long_str)):
        while long_str[right] in char_set:
            char_set.remove(long_str[left])
            left +=1

        char_set.add(long_str[right])
        max_len =  max(max_len, right-left+1)
    return max_len

print(longest_sustring(long_str))