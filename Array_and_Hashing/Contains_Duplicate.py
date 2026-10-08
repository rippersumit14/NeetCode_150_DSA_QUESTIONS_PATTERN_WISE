
"""
Easy


Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

nums = [1,2,3,4,5]

nums.sort()

#for i in range(len(nums)-1):
#if nums[i] != nums[i+1]:
#print("false")
#else:
#print("true")

#Not optimized 44 test cases passed only
#Main reason can be constraints

nums_2 = [3,2,1]




setty_nums2 = set(nums_2)

if setty_nums2 == nums_2:
    print("false")
else:
    print("true")








