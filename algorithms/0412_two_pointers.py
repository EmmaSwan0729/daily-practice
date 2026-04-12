def max_area(height: list[int]) -> int:
    """
        Given an integer array `height` of length n, there are n vertical lines drawn such that
        the two endpoints of the i-th line are (i, 0) and (i, height[i]).

        Find two lines that together with the x-axis form a container that holds the most water.

        Return the maximum amount of water a container can store.

        You may not slant the container.

        Example 1:
            Input: height = [1,8,6,2,5,4,8,3,7]
            Output: 49

        Example 2:
            Input: height = [1,1]
            Output: 1
    """

    left = 0
    right = len(height)-1
    max_water_area = 0

    while left < right:
        width= right - left
        h = min(height[right], height[left])
        area = width * h

        max_water_area = max(max_water_area, area)

        if height[left] < height[right]:
            left +=1
        else:
            right -=1


    return max_water_area

if __name__ == "__main__":
    print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(max_area([1, 1]))  # 1
