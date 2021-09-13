from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        max_summ = nums[0]

        for num in nums[1:]:
            current = max(current + num, num)
            max_summ = max(max_summ, current)

        return max_summ


if __name__ == '__main__':
    assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert Solution().maxSubArray([5, 4, -1, 7, 8]) == 23
