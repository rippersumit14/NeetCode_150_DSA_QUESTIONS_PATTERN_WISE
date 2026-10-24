class Solution:
    def valid_palindrome_II(self, s: str) -> bool:
        # Helper function to check palindrome between left and right
        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False


                left += 1
                right -= 1

            return True

        left = 0
        right = len(s) - 1

        while left < right:
            # if both the characters same, move both pointers
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # mismatch found
                # try skipping the left or right character
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)

        return True

        # time-complexity -> O(n)
        # space-complexity -> O(1)


soly = Solution()
print(soly.valid_palindrome_II("abca"))  # Output: True
print(soly.valid_palindrome_II("abc"))  # Output: False