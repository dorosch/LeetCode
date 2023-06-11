class Solution:
    def fib(self, n: int) -> int:
        return n if n <= 1 else self.fib(n - 1) + self.fib(n - 2)


if __name__ == '__main__':
    assert Solution().fib(2) == 1
    assert Solution().fib(3) == 2
    assert Solution().fib(4) == 3
