from typing import List


class Solution:
    def binarySearch(self, nums: List[int], target: int, left_based: bool) -> int:
        left, right = 0, len(nums) - 1
        result = -1

        while left <= right:
            middle = (left + right) // 2

            if target > nums[middle]:
                left = middle + 1
            elif target < nums[middle]:
                right = middle - 1
            else:
                result = middle

                if left_based:
                    right = middle - 1
                else:
                    left = middle + 1

        return result

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.binarySearch(nums, target, True), self.binarySearch(nums, target, False)]


if __name__ == "__main__":
    assert Solution().searchRange([], 0) == [-1, -1]
    assert Solution().searchRange([1], 1) == [0, 0]
    assert Solution().searchRange([2, 2], 2) == [0, 1]
    assert Solution().searchRange([1, 3, 3, 3, 4], 3) == [1, 3]
    assert Solution().searchRange([1, 3, 3, 3, 3, 3], 3) == [1, 5]
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 5) == [0, 0]
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert Solution().searchRange([1, 2, 3, 3, 3, 10], 3) == [2, 4]
    assert Solution().searchRange([1, 2, 3, 3, 3, 3, 4, 5, 9], 3) == [2, 5]
    assert Solution().searchRange([1, 1, 1, 2, 4, 4, 4, 5, 5, 5, 5, 6, 7, 8, 8, 9, 9, 9, 9, 9, 9, 10], 9) == [15, 20]
