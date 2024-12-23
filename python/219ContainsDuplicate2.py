from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_dict: dict[int, list] = dict()
        for index, item in enumerate(nums):
            if not item in my_dict:
                my_dict[item] = [index]
            else:
                my_dict[item].append(index)

        for li in my_dict.values():
            if len(li) < 2:
                continue

            i = 0
            j = 1
            while j < len(li):
                if abs(li[i] -li[j]) <= k:
                    return True
                i += 1
                j += 1

        return False

solution = Solution()

print(solution.containsNearbyDuplicate([1,0,1,1], 1))
