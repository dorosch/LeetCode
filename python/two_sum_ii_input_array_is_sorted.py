from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = defaultdict(int)

        for index, num in enumerate(numbers):
            if num in hash_map:
                return [hash_map[num] + 1, index + 1]

            hash_map[target - num] = index


if __name__ == '__main__':
    assert Solution().twoSum([2, 3, 4], 6) == [1, 3]
    assert Solution().twoSum([2, 7, 11, 15], 9) == [1, 2]
