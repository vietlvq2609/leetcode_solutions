from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = [-1] * (len(nums) + 1)
        for i in nums:
            arr[i] = i
        return arr.index(-1)

    # Other solution
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n*(n+1)//2
        for num in nums:
            ans-=num
        return ans