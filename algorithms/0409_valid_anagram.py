from collections import Counter

s = "anagram"
t = "nagaram"

def anagram_words(first:str, second:str) -> bool:
    """
    valid two words if  they are anagram.

    Args:
        first: a string.
        second: a string.

    Returns:
        bool.
    """
    if Counter(first) == Counter(second):
        return True
    else:
        return False
    
print(anagram_words(s,t))