from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        return set(b for _, b in paths).difference(a for a, _ in paths).pop()


if __name__ == '__main__':
    assert Solution().destCity([["A", "Z"]]) == "Z"
    assert Solution().destCity([["B", "C"], ["D", "B"], ["C", "A"]]) == "A"
