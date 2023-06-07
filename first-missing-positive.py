from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        number, numbers = 1, set(nums)

        while number in numbers:
            number += 1

        return number


if __name__ == '__main__':
    assert Solution().firstMissingPositive([1, 2, 0]) == 3
    assert Solution().firstMissingPositive([3, 4, -1, 1]) == 2
    assert Solution().firstMissingPositive([7, 8, 9, 11, 12]) == 1
