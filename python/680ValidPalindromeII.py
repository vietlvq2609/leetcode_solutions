class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return is_palindrome(s[left+1:right+1]) or is_palindrome(s[left:right])
            left += 1
            right -= 1
        return True

solution = Solution()
print(solution.validPalindrome("abca"))
