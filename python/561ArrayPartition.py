from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        arr = sorted(nums, reverse = True)
        sum = 0
        for i in range(0, len(nums), 2):
            sum += arr[i+1]
        return sum

solution = Solution()
solution.arrayPairSum([1,4,3,2])