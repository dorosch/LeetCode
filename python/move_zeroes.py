from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        position = 0

        for index, value in enumerate(nums):
            if value != 0:
                nums[position], nums[index] = nums[index], nums[position]
                position += 1


if __name__ == '__main__':
    nums = [0]
    Solution().moveZeroes(nums)

    assert nums == [0]

    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)

    assert nums == [1, 3, 12, 0, 0]
