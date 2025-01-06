from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = 0
        p = 1
        count = 1
        while p < len(nums):
            if nums[p] > nums[ans]:
                count = 1
                ans += 1
                nums[ans] = nums[p]
            elif nums[p] == nums[ans] and count < 2:
                count += 1
                ans += 1
                nums[ans] = nums[p]
            else:
                count += 1
            p += 1
        return ans + 1

    # Other solution
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        i = 2
        for j in range(2, len(nums)):
            if nums[j] != nums[i - 2]:
                nums[i] = nums[j]
                i += 1
        return i

    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for fast in range(len(nums)):
            if slow < 2 or nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
        return slow

solution = Solution()
print(solution.removeDuplicates([1,1,1,2,2,3])) # 5
