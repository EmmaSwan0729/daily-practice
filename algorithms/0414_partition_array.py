nums = [9, 12, 3, 5, 14, 10, 10]
pivot = 10

def partition_array_three(nums: list[int], pivot: int) -> list[int]:
    """
    Partition an array into three parts: < pivot, == pivot, > pivot using the Dutch National Flag algorithm.

    The operation is done in-place using three pointers:
    - low: boundary for elements < pivot
    - mid: current element
    - high: boundary for elements > pivot

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        nums (list[int]): Input array.
        pivot (int): Pivot value for partitioning.

    Returns:
        list[int]: Partitioned array (in-place).
    """
    low,mid,high = 0, 0, len(nums)-1

    while mid <= high:
        if nums[mid] < pivot:
            nums[low], nums[mid] = nums[mid],nums[low]
            low += 1
            mid += 1
        elif nums[mid] == pivot:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1 
    
    return nums

print(partition_array_three(nums, pivot))