from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            middle = left + (right - left) // 2
            value = nums[middle]

            if target < value:
                right = middle - 1
            elif target > value:
                left = middle + 1
            else:
                return middle

        return left if target <= nums[left] else right + 1


if __name__ == '__main__':
    assert Solution().searchInsert([1, 3, 5, 6], 5) == 2
    assert Solution().searchInsert([1, 3, 5, 6], 2) == 1
    assert Solution().searchInsert([1, 3, 5, 6], 7) == 4
    assert Solution().searchInsert([1, 3, 5, 6], 0) == 0
    assert Solution().searchInsert([1], 0) == 0
