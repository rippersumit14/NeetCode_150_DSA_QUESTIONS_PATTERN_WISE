def GroupAnagram(strs: []):
    hashy = {}

    for word in strs:
        key = "".join(sorted(word))
        if key not in hashy:
            hashy[key] = []

        hashy[key].append(word)

    return list(hashy.values())

print(GroupAnagram(["eat", "tea", "tan", "ate", "nat", "bat"]))
#Time_complexity-> o(N x KlogK)
#Space_complexity-> o(N X K)





