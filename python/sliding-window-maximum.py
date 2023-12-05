from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue, result = deque(), []

        for r in range(len(nums)):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()

            queue.append(r)

            if r + 1 < k:
                continue

            if queue[0] < r + 1 - k:
                queue.popleft()

            result.append(nums[queue[0]])

        return result


if __name__ == '__main__':
    assert Solution().maxSlidingWindow([1, -1], 1) == [1, -1]
    assert Solution().maxSlidingWindow([7, 2, 4], 2) == [7, 4]
    assert Solution().maxSlidingWindow([1, 3, 1, 2, 0, 5], 3) == [3,3,2,5]
    assert Solution().maxSlidingWindow(
        [1, 3, -1, -3, 5, 3, 6, 7], 3
    ) == [3, 3, 5, 5, 6, 7]
