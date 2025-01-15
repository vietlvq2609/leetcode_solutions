class Solution:
    # non-tail recursive
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return self.fib(n-1) + self.fib(n-2)

    # tail recursive
    def fib(self, n: int) -> int:
        return self._fib_helper(n, 0, 1)
    def _fib_helper(self, n: int, a: int, b: int) -> int:
        if n == 0:
            return a
        if n == 1:
            return b
        return self._fib_helper(n-1, b, a + b)
