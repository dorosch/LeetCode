from collections import defaultdict
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        a, b = nums1, nums2
        m, n = len(a), len(b)

        if n < m:
            a, b = b, a

        hash_map = defaultdict(int)

        for value in b:
            hash_map[value] += 1

        for value in a:
            if value in hash_map and hash_map[value] > 0:
                hash_map[value] -= 1
                result.append(value)

        return result


if __name__ == '__main__':
    assert Solution().intersect([1, 2, 2, 1], [2, 2]) == [2, 2]
    assert Solution().intersect([3, 1, 2], [1, 1]) == [1]
