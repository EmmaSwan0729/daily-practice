def two_sum(nums:list[int], target:int) -> list[int]:
    seen = {}
    
    for i,num in enumerate(nums):
        first_num = target - num
        if first_num in seen:
            return [seen[first_num],i]
        seen[num] = i 

print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
print(two_sum([3, 2, 4], 6))       # [1, 2]