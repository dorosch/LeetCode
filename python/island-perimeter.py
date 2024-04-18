from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0

        for i, line in enumerate(grid):
            for j, value in enumerate(line):
                if value == 1:
                    perimeter += 4

                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 2

                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 2

        return perimeter


if __name__ == "__main__":
    assert Solution().islandPerimeter([[1]]) == 4
    assert Solution().islandPerimeter([[1, 0]]) == 4
    assert Solution().islandPerimeter([[0, 1]]) == 4
    assert Solution().islandPerimeter(
        [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    ) == 16
