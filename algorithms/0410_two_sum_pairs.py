nums = [2, 7, 4, 0, 3, 4, 5]
target = 7

#双指针方法
def two_sum(nums:list[int], target:int) -> list[list[int]]:
    """
    Find all unique pairs of numbers in the array that sum up to the target.

    Each pair [a, b] must satisfy:
    - a + b == target
    - a <= b
    - No duplicate pairs in the result
    - The result is sorted by 'a' in ascending order

    Args:
        nums (list[int]): List of integers
        target (int): Target sum value

    Returns:
        list[list[int]]: A list of unique pairs [a, b] satisfying the conditions
    """
    nums.sort()
    left, right = 0, len(nums)-1
    result = []

    while left < right:
        curr_sum = nums[left] + nums[right]

        if curr_sum == target:
            result.append([nums[left], nums[right]])

            left_val = nums[left]
            right_val = nums[right]

            while left < right and nums[left] == left_val:
                left += 1
            while left < right and nums[right] == right_val:
                right -= 1
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return result

#哈希表
def two_nums_sum(nums:list[int], target:int) -> list[list[int]]:
    """
    Find all unique pairs of numbers in the array that sum up to the target.

    Each pair [a, b] must satisfy:
    - a + b == target
    - a <= b
    - No duplicate pairs in the result
    - The result is sorted by 'a' in ascending order

    Args:
        nums (list[int]): List of integers
        target (int): Target sum value

    Returns:
        list[list[int]]: A list of unique pairs [a, b] satisfying the conditions
    """
    seen = set()
    result_pair = set()
    result = []

    for first_num in nums:
        sec_num = target - first_num

        if sec_num in seen:
            seen.add(first_num)

            if first_num <= sec_num:
                result_pair.add((first_num, sec_num))

            elif first_num > sec_num:
                first_num, sec_num = sec_num, first_num
                result_pair.add((first_num, sec_num))

        seen.add(first_num)

        result = [list(pair) for pair in sorted(result_pair)]

    return result 

print(two_sum(nums, target))
print(two_nums_sum(nums, target))
