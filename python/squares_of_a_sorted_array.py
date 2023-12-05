from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        left, right = 0, len(nums) - 1

        while left <= right:
            left_value = nums[left] ** 2
            right_value = nums[right] ** 2

            if left_value > right_value:
                result.append(left_value)
                left += 1
            else:
                result.append(right_value)
                right -= 1

        return result[::-1]


if __name__ == '__main__':
    assert Solution().sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert Solution().sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
