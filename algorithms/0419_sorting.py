def merge_sort(arr: list[int]) -> list[int]:
    """
    Sorts a list using the merge sort algorithm.

    Merge sort is a divide-and-conquer algorithm that recursively splits
    the array into halves, sorts each half, and then merges the sorted halves.

    Args:
        arr (list[int]): The list of integers to be sorted.

    Returns:
        list[int]: A new sorted list in ascending order.

    Time Complexity:
        O(n log n) in all cases (best/average/worst)

    Space Complexity:
        O(n) due to auxiliary arrays used during merging
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return _merge(left, right)

def _merge(left: list[int], right: list[int]) -> list[int]:
    """
    Merges two sorted lists into a single sorted list.

    This function compares elements from two sorted lists one by one,
    appending the smaller element to the result list until all elements
    are consumed.

    Args:
        left (list[int]): First sorted list.
        right (list[int]): Second sorted list.

    Returns:
        list[int]: A merged sorted list in ascending order.

    Time Complexity:
        O(n), where n is the total number of elements in both lists.

    Space Complexity:
        O(n)
    """
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])

    return result

print(merge_sort([]))        
print(merge_sort([1]))       
print(merge_sort([3, 1]))   
print(merge_sort([5, 2, 4, 6, 1, 3])) 
