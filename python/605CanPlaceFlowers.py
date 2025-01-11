from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        n = len(flowerbed)
        while i < n:
            if flowerbed[i] == 0:
                if i-1 < 0 and flowerbed[i-1] == 1:
                    i += 1
                    continue
                if i+1 < n and flowerbed[i+1] == 1:
                    i += 1
                    continue
                n -= 1
                flowerbed[i] = 1
            i += 1
        return n <= 0

solution = Solution()
print(solution.canPlaceFlowers([1,0,0,0,0,1], 2))