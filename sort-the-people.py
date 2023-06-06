from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [name for _, name in sorted(zip(heights, names), reverse=True)]


if __name__ == '__main__':
    assert Solution().sortPeople(
        ["Mary", "John", "Emma"], [180, 165, 170]
    ) == ["Mary", "Emma", "John"]
