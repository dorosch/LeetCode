from collections import Counter
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        return [num for num, count in Counter(nums).items() if count > 1]


if __name__ == '__main__':
    assert Solution().findDuplicates([1]) == []
    assert Solution().findDuplicates([1, 1, 2]) == [1]
    assert Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3]
