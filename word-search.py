from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        flag = False

        def is_valid_chain(i: int, j: int, index: int, paths: List):
            if index == len(word):
                nonlocal flag
                flag = True
                return

            for x, y in [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]:
                if (x < 0 or x >= len(board)) or (y < 0 or y >= len(board[x])):
                    continue

                if board[x][y] == word[index] and (x, y) not in paths:
                    is_valid_chain(x, y, index + 1, paths + [(x, y)])

        for i, row in enumerate(board):
            for j, value in enumerate(row):
                if value == word[0]:
                    is_valid_chain(i, j, 1, [(i, j)])

        return flag


if __name__ == '__main__':
    assert Solution().exist([
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ], "SEE")
    assert Solution().exist([
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ], "ABCCED")
    assert not Solution().exist([
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ], "ABCB")
