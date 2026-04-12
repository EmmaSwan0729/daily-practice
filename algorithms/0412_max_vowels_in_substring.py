s = "abciiidef"
k = 3

def max_num_vowels(s:str, k:int) -> int:
    """
    Return the maximum number of vowels in any substring of length k.

    Uses a fixed-size sliding window:
    - Count vowels in the initial window of size k.
    - Slide the window one character at a time.
    - Update the count by removing the left character and adding the right character.

    Args:
        s (str): Input string consisting of lowercase letters.
        k (int): Length of the substring.

    Returns:
        int: Maximum number of vowels in any substring of length k.
    """
    vowels = set("aeiou")

    current_count = 0
    for i in range(k):
        if s[i] in vowels:
            current_count += 1 
    max_count = current_count

    for right in range(k, len(s)):
        left = right -k

        if s[left] in vowels:
            current_count -= 1
        if s[right] in vowels:
            current_count += 1
        
        max_count = max(max_count, current_count)
    return max_count

print(max_num_vowels(s, k))

