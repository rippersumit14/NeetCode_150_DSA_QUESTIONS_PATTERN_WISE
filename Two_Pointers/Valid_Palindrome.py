class Solution:
    def isPalindrome(self, s: str) -> bool:
        """if s == "":
            return True #Edge Case

        Test_1 = ""

        for ch in s:
            if ch.isalnum():
                Test_1 += ch

        Test_1 = Test_1.lower()

        testy = ""

        for i in range(len(Test_1)-1,-1,-1):
            testy += Test_1[i]

        if testy == Test_1:
            return True
        else:
            return False


        #Time_complexity => o(n)
        #Space_complexity => o(n) """ #Further Optimization


        l = 0
        r = len(s)-1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l = l + 1
            r = r - 1

        return True

        #Time_Complexity->o(n)
        #Space_Complexity->o(1)








