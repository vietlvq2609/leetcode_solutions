from typing import List

class Solution:
    # Greedy approach
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        j = 0
        content = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
                content += 1
            j += 1
        return content

