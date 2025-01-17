from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0

        for bill in bills:
            if bill == 5:
                five += 1
                continue

            if bill == 10:
                if five == 0:
                    return False
                ten += 1
                five -= 1
                continue

            if ten > 0:
                if five > 0:
                    ten -= 1
                    five -= 1
                    continue
                else:
                    return False

            if ten == 0:
                if five >= 3:
                    five -= 3
                    continue
                else:
                    return False

        return True