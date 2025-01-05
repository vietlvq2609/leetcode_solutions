from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        p = 0
        ans = 0
        while p < len(nums):
            if nums[p] > nums[ans]:
                ans += 1
                nums[ans] = nums[p]
            p += 1
        return ans + 1