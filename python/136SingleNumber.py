from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seens = set()
        for num in nums:
            if not num in seens:
                seens.add(num)
            else:
                seens.remove(num)
        return seens.pop()

    # faster solution
    def xorSolution(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result