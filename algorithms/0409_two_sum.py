nums = [2, 7, 11, 15]
target = 9

def two_nums_sum(nums: list[int],  target: int) -> list[int]:
    """
    Find two nums in the nums list and return indexes.

    Args:
        nums: A list of integers.
        target: sum of two nums.

    Returns:
        Indexes of two num in the nums list.
    """
    seen = {}
    for i, num in  enumerate(nums):        
        first_num = target - num
        if first_num in seen:
            return [seen[first_num], i]
        seen[num] = i
