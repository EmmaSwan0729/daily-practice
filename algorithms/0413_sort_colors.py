nums = [2,0,2,1,1,0]

def sort_colors(nums:list[int]) -> list[int]:
    """
    Sort an array containing only 0s, 1s, and 2s in-place using the Dutch National Flag algorithm.

    This algorithm uses three pointers:
    - first (low): boundary for 0s
    - second (mid): current element being processed
    - third (high): boundary for 2s

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        nums (list[int]): List of integers containing only 0, 1, and 2.

    Returns:
        list[int]: The sorted list (in-place modification).
    """
    
    first, second, third = 0, 0, len(nums)-1
    
    while second <= third:
        if nums[second] == 0:
            nums[first], nums[second] = nums[second], nums[first]
            first += 1
            second += 1
        elif nums[second] == 1:
            second += 1
        else:
            nums[second], nums[third] = nums[third],nums[second]
            third -= 1

    return nums

print(sort_colors(nums))