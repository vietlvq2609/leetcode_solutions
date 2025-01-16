class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        char_count = {char: 0 for char in s}
        for char in s:
            char_count[char] += 1

        stack = []
        in_stack = set()

        for char in s:
            char_count[char] -= 1
            if char in in_stack:
                continue
            while stack and stack[-1] > char and char_count[stack[-1]] > 0:
                removed = stack.pop()
                in_stack.remove(removed)
            stack.append(char)
            in_stack.add(char)

        return ''.join(stack)

solution = Solution()
print(solution.removeDuplicateLetters("cbacdcbc")) # "acdb"
