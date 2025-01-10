from typing import List

class Solution:
    # Gready approach
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0
        for i in range(len(nums)):
            if i > max_reachable:
                return False
            max_reachable = max(max_reachable, i + nums[i])
            if max_reachable >= len(nums) - 1:
                return True
        return False

    # Gready approach 2
    def canJump(self, nums: List[int]) -> bool:
        goal = 0
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

    # Dynamic programming approach
    def canJumpDP(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        for i in range(n):
            if dp[i]:
                for j in range(i + 1, min(i + nums[i] + 1, n)):
                    dp[j] = True
        return dp[n - 1]

solution = Solution()
nums = [3,2,1,0,4]
print(solution.canJump(nums)) # True