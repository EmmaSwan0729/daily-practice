nums =  [0, 1, 0, 3, 12]

def move_zero_to_end(nums:list[int]) -> None:
    """
    Move all of the zeros to the end of list.

    Args:
        nums: A list of integers.

    Returns:
        None.
    """
    left  = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left +=1