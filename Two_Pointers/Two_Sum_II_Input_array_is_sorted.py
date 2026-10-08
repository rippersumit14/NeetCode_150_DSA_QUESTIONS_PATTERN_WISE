def two_sum_2_INputArr_is_sorted(nums: [], target: int):


    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j] and nums[i] + nums[j] == target:
                return i, j


    #Time_complexity => o(n^2)
    #Space_complexity => o(1)

#Optimized Way
def optimized_two_pointers(nums: [], target: int):
    low = 0
    fast = len(nums) - 1

    while low < fast:
        current_sum = nums[low] + nums[fast]
        if current_sum == target:
            return [low+1, fast+1]
        if current_sum > target:
            fast -= 1
        if current_sum < target:
            low += 1





print(optimized_two_pointers([2,3,4], 6))


