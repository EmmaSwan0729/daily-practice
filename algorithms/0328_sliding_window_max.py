
import pandas as pd

def sliding_window_max(nums:list[int], k:int) -> list[int]:

    # 返回每个滑动窗口中的最大值列表。
    # Args:
    #     nums: 输入整数列表
    #     k: 窗口大小
    # Returns:
    #     每个窗口最大值组成的列表

    results=[]

    for i in range(len(nums)-k+1):
        list_window = nums[i:i+k]
        list_max = max(list_window)

        results.append(list_max)

    return results

nums = [1, 3, -1, -3, 5, 3, 6, 7]
print(sliding_window_max(nums, 3)) # [3, 3, 5, 5, 6, 7]
