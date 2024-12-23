from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return nums[0]

        store = dict()

        max = nums[0]
        store[max] = 1

        for i in range(1, len(nums)):
            if nums[i] in store:
                store[nums[i]] += 1
            else:
                store[nums[i]] = 1

            if store[nums[i]] > store[max]:
                max = nums[i]

        return max

solution = Solution()

print(solution.majorityElement([2,2,1,1,1,2,2]))
