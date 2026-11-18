"""
Given an array
Find the largest element in an array


nums = [1,2,3]
output = 3


*Without using the in_built function of Python
"""

nums = [1,2,3]


def max_number(nums: []):
    nums.sort()

    maxy = 0

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] <= nums[j]:
                maxy = nums[j]

    return maxy

#Time_complexity -> o(n^2)
#Space_complexity -> o(n)


print(max_number([42,2,4,6,2,44,243,2]))
