#Given an integer array nums,
#Return all the triplets that are == 0
from Array_and_Hashing.Contains_Duplicate import nums


def three_sum(nums: []):
    nums.sort()

    extra_arr = set() #Triplets are not repeated

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for z in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[z] == 0:
                    extra_arr.add((nums[i], nums[j], nums[z]))

    return extra_arr
print(three_sum([-1,0,1,2,-1,-4]))

#Time Complexity => o(n^3)
#Space Complexity => o(n^3)

#One another Unoptimzed way
def ThreeSUMYUn(nums: []):
    res = []
    nums.sort()

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue

        l = i + 1
        r = len(nums) - 1

        while l < r:
            threeSUM = a + nums[l] + nums[r]
            if threeSUM > 0:
                r -= 1
            elif threeSUM < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1

        return res

    #Time_complexity -> o(n^2)
    #Space_complexity -> o(1)/o(n)









#Optimized Way Using two pointers
def optimized_three_Sum(nums: []):

    nums.sort()


    current = 0
    current_one = 1
    fasty = len(nums) - 1

    #Creating lists of lists
    final_list = [[]]

    while current < fasty:
        if nums[current] + nums[current_one] + nums[fasty] == 0:
            final_list.append([nums[current], nums[current_one], nums[fasty]])
        else:
            current += 1
            current_one += 1
            fasty -= 1

    return final_list

print(optimized_three_Sum([-1,0,1,2,-1,-4]))















