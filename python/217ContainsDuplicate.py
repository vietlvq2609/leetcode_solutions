from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for i in nums:
            if i in seen:
                return True
            seen.add(i)

        return False

solution = Solution()

print(solution.containsDuplicate([1,2,3,1]))
