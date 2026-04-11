numbers = [2, 7, 11, 15]
target = 9

def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    """
    Find two numbers in a sorted array that add up to the target.

    Uses a two-pointer approach:
    - Start with one pointer at the beginning and one at the end.
    - If the sum is too large, move the right pointer left.
    - If the sum is too small, move the left pointer right.
    - Continue until the target sum is found.

    The returned indices are 1-indexed.

    Args:
        numbers (list[int]): A list of integers sorted in ascending order.
        target (int): Target sum.

    Returns:
        list[int]: Indices (1-based) of the two numbers that add up to target.
    """
    left = 0
    right = len(numbers) - 1

    while left < right:  # 这是双指针，两个都动，控制过程
        current_sum = numbers[left] + numbers[right] 

    # for num in numbers: # 这是遍历数组，
    #     current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left+1, right+1]
        elif current_sum > target:
            right -= 1
        else:
            left += 1
        
print(two_sum_sorted(numbers, target))



