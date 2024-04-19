from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        n, m = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m:
                return

            if grid[i][j] in ("-1", "0"):
                return

            grid[i][j] = "-1"

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)


        for i, line in enumerate(grid):
            for j, value in enumerate(line):
                if value == "1":
                    dfs(i, j)
                    islands += 1

        return islands


if __name__ == "__main__":
    assert Solution().numIslands([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]) == 1
    assert Solution().numIslands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]) == 3
