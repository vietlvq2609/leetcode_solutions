from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        total_profit = 0
        p1 = 0
        p2 = 1
        while p2 < len(prices):
            if prices[p2] > prices[p1]:
                total_profit += prices[p2] - prices[p1]
                p1 = p2
            elif prices[p2] < prices[p1]:
                p1 = p2
            p2 += 1
        return total_profit


solution = Solution()
prices = [7,1,5,3,6,4]
print(solution.maxProfit(prices)) # 7