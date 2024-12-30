from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        if self.q1:
            while self.q1:
                curr = self.q1.pop(0)
                if not self.q1:
                    return curr
                self.q2.append(curr)
        else:
            while self.q2:
                curr = self.q2.pop(0)
                if not self.q2:
                    return curr
                self.q1.append(curr)

    def top(self) -> int:
        if self.q1:
            while self.q1:
                curr = self.q1.pop(0)
                self.q2.append(curr)
                if not self.q1:
                    return curr
        else:
            while self.q2:
                curr = self.q2.pop(0)
                self.q1.append(curr)
                if not self.q2:
                    return curr

    def empty(self) -> bool:
        return not (self.q1 or self.q2)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()