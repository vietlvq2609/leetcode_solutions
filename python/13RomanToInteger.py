class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        for i in range(0, len(s)):
            if i+1 == len(s):
                total += self.intFromRoman(s[i])
                break
            if self.intFromRoman(s[i+1]) > self.intFromRoman(s[i]):
                total -= self.intFromRoman(s[i])
            else:
                total += self.intFromRoman(s[i])
        return total



    def intFromRoman(self, r: str) -> int:
        if r == 'I':
            return 1
        if r == 'V':
            return 5
        if r == 'X':
            return 10
        if r == 'L':
            return 50
        if r == 'C':
            return 100
        if r == 'D':
            return 500
        if r == 'M':
            return 1000
        return -1