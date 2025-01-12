from typing import List

class Solution:
    # Backward greedy solution
    def jumpBackward(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        i = len(nums)-1
        stack = [i]

        while i >= 0:
            for index, item in enumerate(stack):
                if nums[i] + i >= item:
                    stack = stack[:index+1] + [i]
                    break
            i -= 1

        return len(stack) - 1

    # Forward greedy solution (more efficient)
    def jumpForward(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        jumps = 0
        farthest = 0
        current_end = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
                if current_end >= n - 1:
                    break

        return jumps

solution = Solution()
print(solution.jumpForward([2,3,1,1,4])) # 2