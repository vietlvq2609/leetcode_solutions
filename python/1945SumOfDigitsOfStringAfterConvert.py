class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = ""
        for letter in s:
            num += str(self.letter_to_number(letter))

        for _ in range(k):
            num = str(sum(int(digit) for digit in num))

        return int(num)

    def letter_to_number(self, letter: str) -> int:
        return ord(letter.lower()) - ord('a') + 1

solution = Solution()

solution.getLucky("iiii", 1)
