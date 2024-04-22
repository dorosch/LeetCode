from typing import List
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        solutions = set()
        visited = set()
        deadends = set(deadends)

        def rotate(code: str, index: int, forward=True):
            if forward:
                value = str((int(code[index]) + 1) % 10)
            else:
                value = str((int(code[index]) - 1) % 10)

            return code[:index] + value + code[index + 1:]


        queue = deque([("0000", 0)])

        while queue:
            code, level = queue.popleft()

            if code in visited or code in deadends:
                continue
            else:
                visited.add(code)

            if code == target:
                solutions.add(level)

            for index in range(4):
                queue.append((rotate(code, index), level + 1))
                queue.append((rotate(code, index, forward=False), level + 1))

        return min(solutions) if solutions else -1


if __name__ == "__main__":
    assert Solution().openLock(
        ["8888"], "0009"
    ) == 1
    assert Solution().openLock(
        ["0201", "0101", "0102", "1212", "2002"], "0202"
    ) == 6
    assert Solution().openLock(
        ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888"
    )== -1
