#Given an integer array nums, return an array such that answer[i] is equal to the product of all the elements of nums except nums[i]

def product_of_array(nums: []):
    n = len(nums)
    res = [1] * n

    for i in range(n):
        for j in range(n):
            if i != j:
                res[i] *= nums[j]

    return res
print(product_of_array([-1,3,2,1]))
#Unoptimized approach
#Time complexity -> o(n^2)
#Space complexity -> o(n)

#Optimized approach
def product_of_array_optimized_approach(nums: []):
    res = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res
#Time-complexity -> o(n)
#Space_complexity -> o(1)

