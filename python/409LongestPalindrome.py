class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        hash_map = {}
        for letter in s:
            if letter in hash_map:
                hash_map[letter] += 1
            else:
                hash_map[letter] = 1
        odd = False
        for key in hash_map:
            ans += hash_map[key] // 2  * 2
            if hash_map[key] % 2 == 1:
                odd = True
        if odd:
            ans += 1
        return ans

solution = Solution()
print(solution.longestPalindrome("abccccdd"))