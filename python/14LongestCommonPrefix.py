from typing import List

class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        prefix = ""
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first), len(last))):
            if(first[i] != last[i]):
                return prefix
            prefix += first[i]
        return prefix