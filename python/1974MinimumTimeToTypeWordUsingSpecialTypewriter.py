class Solution:
    def minTimeToType(self, word: str) -> int:
        sum = 0
        timeToWrite = 1
        prevPosition = ord("a")
        for letter in word:
            curPosition = ord(letter)
            goFromRight = abs(curPosition - prevPosition)
            goFromLeft = 26 - goFromRight
            steps = min(goFromLeft, goFromRight)
            sum += steps + timeToWrite
            prevPosition = curPosition
        return sum

solution = Solution()
print(solution.minTimeToType("bza"))