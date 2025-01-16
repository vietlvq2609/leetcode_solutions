from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_volume = 0

        while left < right:
            x = right - left
            y = min(height[left], height[right])
            max_volume = max(max_volume, x*y)
            while height[left] <= y and left < right:
                left += 1
            while height[right] <= y and left < right:
                right -= 1

        return max_volume
