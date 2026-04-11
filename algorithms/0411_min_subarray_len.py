nums = [2, 3, 1, 2, 4, 3] 
target = 7

def min_subarray_len(target: int, nums: list[int]) -> int:
    """
    Return the minimal length of a contiguous subarray of which the sum is
    greater than or equal to target. If no such subarray exists, return 0.

    Uses a sliding window approach:
    - Expand the window by moving the right pointer.
    - Shrink the window from the left while the current sum >= target
      to find the smallest valid window.

    Args:
        target (int): Target sum.
        nums (list[int]): List of positive integers.

    Returns:
        int: The minimal length of a valid subarray, or 0 if none exists.
    """
    left = 0
    min_length = float('inf')
    current_sum = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return 0 if min_length == float('inf') else min_length

print(min_subarray_len(target,nums))