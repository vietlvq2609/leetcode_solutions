class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            n = self.sum_of_squares(n)
            if n in seen:
                return False
            seen.add(n)
        return True

    def sum_of_squares(self, n):
        return sum(int(digit) ** 2 for digit in str(n))
