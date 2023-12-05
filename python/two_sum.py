from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = defaultdict(int)

        for index, num in enumerate(nums):
            if num in hash_map:
                return [hash_map[num], index]

            hash_map[target - num] = index


if __name__ == '__main__':
    assert set(Solution().twoSum([3, 3], 6)) == {0, 1}
    assert set(Solution().twoSum([2,7,11,15], 9)) == {0, 1}
