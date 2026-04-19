
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

# 注意这一题跟前面两数之和的不一样，这一题的数组是升序排列的，是有顺序的。
# 上面这个方法叫双指针，在algorithms/0409_two_sum.py 中用的叫哈希。
# 哈希（hash）就是：把数据映射成一个“键 → 值”的结构，用一个函数把key转成位置（index），实现 O(1) 查找
# 哈希快，因为它不用遍历，直接定位位置。
# 常见结构：dict{}, set()


