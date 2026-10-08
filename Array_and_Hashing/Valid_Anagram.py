class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Given two strings s and t, return true if t is an anagram of s, and false otherwise

        # Edge case
        if len(s) != len(t):
            return False

        # Creating an extra memory
        stack_s = []
        stack_t = []

        for i in s:
            stack_s.append(i)

        for i in t:
            stack_t.append(i)

        freq_of_s = {}

        for i in stack_s:
            if i in freq_of_s:
                freq_of_s[i] += 1
            else:
                freq_of_s[i] = 1

        freq_of_t = {}


        for char in stack_t:
            if char in freq_of_t:
                freq_of_t[char] += 1
            else:
                freq_of_t[char] = 1

        # Final output
        if freq_of_t == freq_of_s:
            return True
        else:
            return False

        # Time_complexity => O(N)
        # Space_complexity => O(N)