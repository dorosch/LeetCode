from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        """Find minimum falling sum.

        Args:
            grid: n x n matrix of integers.

        Returns:
            integer of minimum falling sum.
        """

        n = len(grid)
        row = grid[0]

        for i in range(1, n):
            left = row.index(min(row))
            right = row.index(min(row[:left] + row[left+1:]))

            for j in range(n):
                grid[i][j] += row[left] if j != left else row[right]

            row = grid[i]

        return min(row)


if __name__ == "__main__":
    assert Solution().minFallingPathSum([[7]]) == 7
    assert Solution().minFallingPathSum(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ) == 13
    assert Solution().minFallingPathSum([
        [-73, 61, 43, -48, -36],
        [3, 30, 27, 57, 10],
        [96, -76, 84, 59, -15],
        [5, -49, 76, 31, -7],
        [97, 91, 61, -46, 67]
    ]) == -192
