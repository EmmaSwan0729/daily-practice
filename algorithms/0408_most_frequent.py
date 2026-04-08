from collections import Counter

nums = [1, 3, 2, 3, 1, 3]

def most_frequent(nums: list[int]) -> int:
    num_count = Counter(nums)
    return num_count.most_common(1)[0][0]

print(most_frequent(nums))

def most_frequent_num(nums:list[int]) -> int:
    counts = {}
    for num in nums:
        if num not in counts:
            counts[num] = 0
        counts[num] +=1
    return max(counts, key=counts.get)
    # max(counts)求字典里key 最大的；max(counts, key=counts.get)，第二个参数是求 counts字典里value 最大的。
    # dict.get 本身是一个“函数”（方法）,只有加上参数才会返回 value,d.get(1) 获得key是1的value.
print(most_frequent_num(nums))
