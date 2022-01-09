from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if left == right:
                break

            if nums[left] <= nums[middle]:
                if nums[middle] <= nums[right]:
                    right = middle
                else:
                    left = middle + 1
            else:
                if nums[middle] >= nums[right]:
                    left = middle

                else:
                    right = middle

        return nums[left]


if __name__ == "__main__":
    assert Solution().findMin([3, 1, 2]) == 1
    assert Solution().findMin([5, 1, 2, 3, 4]) == 1
    assert Solution().findMin([3, 4, 5, 1, 2]) == 1
    assert Solution().findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert Solution().findMin([11, 13, 15, 17]) == 11
