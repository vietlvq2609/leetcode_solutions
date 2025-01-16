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

    # iterative solution
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

    # iterative solution optimized
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        prevPrev, prev, curr = 0, 1, 0

        for i in range(2, n+1):
            curr = prevPrev + prev
            prevPrev = prev
            prev = curr

        return curr
