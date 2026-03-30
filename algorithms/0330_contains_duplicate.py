def contains_duplicate(nums:list[int]) -> bool:
    """
    Check if any value appears more than once in the list.
    Args:
        nums: List of integers to check.
    Returns:
        True if any value appears more than once, False otherwise.
    """
    return len(nums) > len(set(nums))
    