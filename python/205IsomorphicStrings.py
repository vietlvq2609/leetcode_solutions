class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = dict()
        ptr = 0
        while ptr < len(s):
            if s[ptr] not in map:
                if t[ptr] in map.values():
                    return False
                map[s[ptr]] = t[ptr]
            else:
                if map[s[ptr]] != t[ptr]:
                    return False
            ptr += 1
        return True

solution = Solution()
print(solution.isIsomorphic("paper", "title"))