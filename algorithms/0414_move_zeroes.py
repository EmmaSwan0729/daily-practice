nums = [0,1,0,3,12]
# 输出: [1,3,12,0,0]

def move_zeros(nums:list[int]) -> list[int]:
    """
    Move all zeros in the array to the end while maintaining the relative order of non-zero elements.

    Uses the two-pointer technique:
    - left: position to place next non-zero
    - right: current scanning index

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        nums (list[int]): Input array.

    Returns:
        list[int]: Modified array (in-place).
    """
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1