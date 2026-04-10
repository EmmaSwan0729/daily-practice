from collections import defaultdict

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

def group_anagram(strs:list[str]) -> list[list[str]]:
    """
    Group all anagrams in the given list of strings.

    An anagram is defined as a word formed by rearranging the letters of another,
    using all original letters exactly once.

    This function groups strings that are anagrams of each other by using a
    sorted version of each string as a key.

    Args:
        strs (list[str]): A list of lowercase strings

    Returns:
        list[list[str]]: A list of groups, where each group contains strings
                         that are anagrams of each other
    """
    groups = defaultdict(list)
    
    for s in strs:
        key = ''.join(sorted(s))
        groups[key].append(s)    
    return list(groups.values())
