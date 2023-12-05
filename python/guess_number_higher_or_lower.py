pick = None


def guess(num: int) -> int:
    if num < pick:
        return -1
    elif num > pick:
        return 1

    return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 0, n

        while left <= right:
            middle = left + (right - left) // 2
            target = guess(middle)

            if target < 0:
                right = middle - 1
            elif target > 0:
                left = middle + 1
            else:
                return middle


if __name__ == "__main__":
    pick = 6
    assert Solution().guessNumber(10) == 6

    pick = 1
    assert Solution().guessNumber(1) == 1

    pick = 1
    assert Solution().guessNumber(2) == 1

    pick = 328
    assert Solution().guessNumber(2) == 328
