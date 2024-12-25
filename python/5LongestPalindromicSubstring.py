class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        longestStr = s[0]
        for index, item in enumerate(s):
            left = right = index
            while left > 0 and s[left-1] == item:
                left -= 1
            while right < len(s) - 1 and s[right+1] == item:
                right += 1
            while left > 0 and right < len(s) - 1 and s[left-1] == s[right+1]:
                left -= 1
                right += 1
            if right - left + 1 > len(longestStr):
                longestStr = s[left:right+1]
        return longestStr

    # Expand Around Center Solution
    def longestPalindromeSolution2(self, s: str) -> str:
        if len(s) < 2:
            return s
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        longestStr = ""
        for i in range(len(s)):
            palindrome1 = expandAroundCenter(i, i)
            palindrome2 = expandAroundCenter(i, i + 1)
            longestStr = max(longestStr, palindrome1, palindrome2, key=len)
        return longestStr

solution = Solution()
print(solution.longestPalindrome("babad"))