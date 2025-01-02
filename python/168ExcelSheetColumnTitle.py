class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            columnNumber -= 1
            result = self.convertNumberToLetter(columnNumber % 26) + result
            columnNumber //= 26
        return result

    def convertNumberToLetter(self, num):
        return chr(num + 65)