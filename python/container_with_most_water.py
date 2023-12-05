from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_volume = 0
        left, right = 0, len(height) - 1

        while left < right:
            new_volume = min(height[left], height[right]) * (right - left)
            max_volume = max(new_volume, max_volume)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_volume


if __name__ == '__main__':
    assert Solution().maxArea([2, 3]) == 2
    assert Solution().maxArea([1, 1]) == 1
    assert Solution().maxArea([0, 1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert Solution().maxArea([4, 3, 2, 1, 4]) == 16
