bad = 4


def isBadVersion(version: int) -> bool:
    return version >= bad


class Solution:
    def firstBadVersion(self, n: int):
        left, right = 1, n

        while left <= right:
            if left == right:
                return left

            middle = left + (right - left) // 2

            if isBadVersion(middle):
                right = middle
            else:
                left = middle + 1


if __name__ == '__main__':
    assert Solution().firstBadVersion(6) == 4
