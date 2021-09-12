from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2

            if target < nums[middle]:
                right = middle - 1
            elif target > nums[middle]:
                left = middle + 1
            else:
                return middle

        return -1


if __name__ == '__main__':
    assert Solution().search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert Solution().search([-1, 0, 3, 5, 9, 12], 2) == -1
