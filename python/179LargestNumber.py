from typing import List
from functools import cmp_to_key

class Solution:
    def compare(self, x, y):
        if x + y > y + x:
            return -1
        if x + y < y + x:
            return 1
        return 0

    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(self.compare))
        if nums[0] == "0":
            return "0"
        return ''.join(nums)
