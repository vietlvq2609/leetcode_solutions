class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while start < end:
            while not s[start].isalnum() and start < end:
                start += 1
            while not s[end].isalnum() and start < end:
                end -= 1
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True

    # Simpler solution
    def isPalindrome(self, s: str) -> bool:
        filtered_s = ''.join(c.lower() for c in s if c.isalnum())
        return filtered_s == filtered_s[::-1]

solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))