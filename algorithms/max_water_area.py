def min_subarray_len(target: int, nums: list[int]) -> int:
    """
    Given an array of positive integers nums and a positive integer target,
    return the minimal length of a contiguous subarray of which the sum is
    greater than or equal to target. If there is no such subarray, return 0.

    Example 1:
        Input: target = 7, nums = [2,3,1,2,4,3]
        Output: 2  # [4,3]

    Example 2:
        Input: target = 4, nums = [1,4,4]
        Output: 1

    Example 3:
        Input: target = 11, nums = [1,1,1,1,1,1,1,1]
        Output: 0
    """

    min_sum = 0
    left = 0
    min_length = float('inf')
    curr_sum = 0

    for right in range(len(nums)):
        curr_sum += nums[right]

        while curr_sum >= target:        
            min_length = min(min_length, right-left+1)
            curr_sum -= nums[left]
            left += 1
    return 0 if min_length == float('inf') else min_length
        
if __name__ == "__main__":
    print(min_subarray_len(7, [2,3,1,2,4,3]))  # 2
    print(min_subarray_len(4, [1,4,4]))        # 1
    print(min_subarray_len(11, [1,1,1,1,1,1,1,1]))  # 0
