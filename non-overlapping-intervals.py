from math import inf
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]], pointer=-inf, answer=0) -> int:
        return answer \
            if not intervals \
            else self.eraseOverlapIntervals(sorted(intervals, key=lambda x: x[1])[1:], sorted(intervals, key=lambda x: x[1])[0][1], answer) \
                if sorted(intervals, key=lambda x: x[1])[0][0] >= pointer \
                else self.eraseOverlapIntervals(sorted(intervals, key=lambda x: x[1])[1:], pointer, answer+1)


if __name__ == '__main__':
    assert Solution().eraseOverlapIntervals([[1, 2], [2, 3]]) == 0
    assert Solution().eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2
    assert Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert Solution().eraseOverlapIntervals([[1, 100], [11, 22], [1, 11], [2, 12]]) == 2
