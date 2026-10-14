#Given an integer array nums, and an integer k, return the k most frequent elements

"""
nums = [1,1,1,2,2,3]

output = [1,2]
"""
#Used Bucket Sort Approach

def Top_k_Freq_elements(nums: [], k: int):

    res = []
    freq = {}

    bucket = []

    for i in range(len(nums)+1):
        bucket.append([])

    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for key, value in freq.items():
        bucket[value].append(key)

    for i in range(len(bucket)-1,0,-1): #Reverse order traversing
       for num in bucket[i]:
           res.append(num)

           if len(res) == k:
                return res

    return res



print(Top_k_Freq_elements([1,2,1,2,3,1,3,2], 2))

#Time_complexity->o(n)
#Space_complexity->o(n)

