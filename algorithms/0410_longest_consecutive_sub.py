nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

def longest_consecutive(nums: list[int]) -> int:
    """
    Find the length of the longest consecutive sequence in an unsorted integer array.

    A consecutive sequence is defined as a sequence of numbers where each number
    differs by 1 (e.g., 1, 2, 3, 4).

    The algorithm uses a set to achieve O(1) lookups and only starts counting
    when a number is the beginning of a sequence (i.e., num - 1 is not in the set).

    Args:
        nums (list[int]): A list of integers (unsorted)

    Returns:
        int: The length of the longest consecutive sequence
    """
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:
            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1
            longest = max(longest, length)
    return longest

print(longest_consecutive(nums))

