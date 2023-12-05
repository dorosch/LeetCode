from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k, n = k % len(nums), len(nums)

        if k:
            self.reverse(nums, 0, n - 1)
            self.reverse(nums, 0, k - 1)
            self.reverse(nums, k, n - 1)

    def reverse(self, nums: List[int], left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(nums, 3)

    assert nums == [5, 6, 7, 1, 2, 3, 4]

    nums = [-1, -100, 3, 99]
    Solution().rotate(nums, 2)

    assert nums == [3, 99, -1, -100]
