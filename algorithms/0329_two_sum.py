# 输入: nums = [2, 7, 11, 15], target = 9
# 输出: [0, 1]
# 解释: nums[0] + nums[1] = 2 + 7 = 9

# def sum_two_nums(nums: list[int], target: int) -> list[int]:
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i,j]

# nums = nums = [2, 7, 11, 15]
# target = 9
# print(sum_two_nums(nums, target)) # [0, 1]


def sum_two_nums(nums:list[int], target:int) -> list[int]:
    seen= {}   # 这是一个字典，手动创建的一个查找表
    for i, num in enumerate(nums):
        complement = target - num   # 得到的是一个值
        if complement in seen:
            return [seen[complement], i]  #seen[complement]拿到的是下标
            # seen是把 num 作为 key, i 作为 value 存起来的字典。
        seen[num] = i # 拿到的也是下标
        # 在第二次循环时因为 if 成立所以直接return

nums = nums = [2, 7, 11, 15]
target = 9
print(sum_two_nums(nums, target)) # [0, 1]