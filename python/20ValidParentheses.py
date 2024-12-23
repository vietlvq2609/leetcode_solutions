class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        mystack = list()
        for i in s:
            if self.isCloseBracket(i):
                if not mystack or i != self.closeBracketOf(mystack[-1]):
                    return False
                else:
                    mystack.pop()
            else:
                mystack.append(i)
        if not mystack:
            return True
        return False

    def closeBracketOf(self, c: str) -> str:
        switcher = {
            "[" : "]",
            "(" : ")",
            "{" : "}"
        }
        return switcher.get(c, "Null")
    def isCloseBracket(self, c: str) -> bool:
        if c in ["]", "}", ")"]:
            return True
        else:
            return False