
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# 输出：6（子数组 [4, -1, 2, 1] 的和最大）

# nums = [1]
# # 输出：1

# nums = [-1, -2, -3]
# # 输出：-1

def max_subarray(nums:list[int]) -> int:
    current = nums[0]
    max_sum = nums[0]
    for num in nums[1:]:
        current = max(num, current + num)
        max_sum = max(max_sum, current)
    return max_sum

print(max_subarray(nums))


