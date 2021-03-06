class Solution:
    def pow(self, x: float, n: int) -> float:
        if x == 0:
            return 0

        if n == 0:
            return 1

        result = self.pow(x, n // 2)
        result *= result

        return x * result if n % 2 else result

    def myPow(self, x: float, n: int) -> float:
        result = self.pow(x, abs(n))

        return result if n >= 0 else 1 / result


if __name__ == '__main__':
    Solution().myPow(0.00001, 2147483647)
