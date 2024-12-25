from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        result = []
        for num in nums:
            if result == []:
                result.append([num, num])
            elif num == result[-1][1] + 1:
                result[-1][1] = num
            else:
                if result[-1][0] != result[-1][1]:
                    result[-1] = f"{result[-1][0]}->{result[-1][1]}"
                else:
                    result[-1] = str(result[-1][0])
                result.append([num, num])
        if result[-1][0] != result[-1][1]:
            result[-1] = f"{result[-1][0]}->{result[-1][1]}"
        else:
            result[-1] = str(result[-1][0])
        return result

    # Other solution
    def solution2(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        result = []
        start = nums[0]
        for i in range(1, len(nums) + 1):
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{nums[i - 1]}")
                if i < len(nums):
                    start = nums[i]
        return result

solution = Solution()
print(solution.summaryRanges([0,1,2,4,5,7]))