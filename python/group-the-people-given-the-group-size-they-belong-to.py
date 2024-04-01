from typing import List
from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result = []
        groups = defaultdict(list)

        for index, size in enumerate(groupSizes):
            if len(groups[size]) < size:
                groups[size].append(index)
            else:
                result.append(groups[size])
                groups[size] = [index]

        return result + list(groups.values())


if __name__ == "__main__":
    assert sorted(Solution().groupThePeople([2, 1, 3, 3, 3, 2])) == sorted([[1], [0, 5], [2, 3, 4]])
    assert sorted(Solution().groupThePeople([3, 3, 3, 3, 3, 1, 3])) == sorted([[5], [0, 1, 2], [3, 4, 6]])
