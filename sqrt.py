class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x

        if x < 2:
            return x

        while left < right:
            middle = left + (right - left) // 2
            target = round(middle * middle)

            if x < target:
                right = middle
            elif x > target:
                left = middle + 1
            else:
                return middle

        return left - 1


if __name__ == "__main__":
    assert Solution().mySqrt(1) == 1
    assert Solution().mySqrt(4) == 2
    assert Solution().mySqrt(8) == 2
    assert Solution().mySqrt(24) == 4
    assert Solution().mySqrt(1792844963) == 42341
