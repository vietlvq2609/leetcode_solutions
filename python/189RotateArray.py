from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

    # Use additional memory (Not accepted)
    def rotateAdditionalMemory(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        arr = nums[n-k: n] + nums[0: n-k+1]
        for i in range(n):
            nums[i] = arr[i]

solution = Solution()
nums = [1,2,3,4,5,6,7]
solution.rotate(nums, 3)
