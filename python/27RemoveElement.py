from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            if nums[0] == val:
                return 0
            return 1
        start, end = 0, len(nums) - 1
        while start < end:
            while start < end and nums[start] != val:
                start += 1
            while start < end and nums[end] == val:
                end -= 1
            if nums[start] == nums[end] and nums[start] != val:
                start += 1
            else:
                nums[start] = nums[end]
                nums[end] = val
        return start

    # Simpler and more efficient solution
    def removeElement(self, nums: List[int], val: int) -> int:
        position = 0
        for num in nums:
            if num != val:
                nums[position] = num
                position += 1
        return position


solution = Solution()
print(solution.removeElement([3, 3], 5))