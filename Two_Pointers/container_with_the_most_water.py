def maxArea(height: []) -> int:
    #Height = [1,8,6,2,5,4,8,3,7]
    left = 0
    right = len(height) - 1

    maxy = 0

    while left < right:
        Current_area = (right - left) * min(height[left], height[right])
        maxy = max(Current_area, maxy)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maxy

print(maxArea([1,8,6,2,5,4,8,3,7]))