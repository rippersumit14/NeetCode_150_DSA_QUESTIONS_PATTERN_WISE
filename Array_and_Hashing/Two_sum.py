"""
Given
nums = [2,7,11,15], Target = 9

return the indices of the two numbers that are equal to the target

0 and 1

"""

def two_sum(nums: [], target: int):

    freq = {}

    for i in range(len(nums)):
        current_number = nums[i]
        complement = target - current_number

        if complement in freq:
            return [freq[complement], i]
        else:
            freq[current_number] = i



print(two_sum([2,7,11,15], 9))

#O(n) Time complexity
#O(n) Space complexity

