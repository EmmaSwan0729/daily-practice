
numbers = [2,7,11,15]
target = 9

def two_sum(nums:list[int], target:int) -> list[int]:
    """
    Find two numbers in a sorted array that add up to a target using the two-pointer technique.

    The array is assumed to be sorted in ascending order.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        nums (list[int]): Sorted list of integers.
        target (int): Target sum.

    Returns:
        list[int]: 1-based indices of the two numbers.
    """
    left, right = 0, len(nums)-1

    while left < right:
        s = nums[left] + nums[right]

        if s == target:
            return [left+1, right+1]
        elif s < target:
            left += 1
        else:
            right -= 1

print(two_sum(numbers, target))



