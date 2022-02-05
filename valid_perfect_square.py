class Solution:
    def sqrt(self, x: int) -> int:
        left, right = 1, x

        if x < 2:
            return x

        while left < right:
            middle = (left + right) // 2
            target = round(middle * middle)

            if x < target:
                right = middle
            elif x > target:
                left = middle + 1
            else:
                return middle

        return left - 1

    def isPerfectSquare(self, num: int) -> bool:
        result = self.sqrt(num)

        return result * result == num


if __name__ == '__main__':
    assert Solution().isPerfectSquare(16)
    assert not Solution().isPerfectSquare(15)
