from typing import List
from collections import defaultdict, deque


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Recursion solution
        # def dfs(node) -> bool:
        #     if node == destination:
        #         return True
        #     visited.add(node)
        #     return any(dfs(x) for x in graph[node] if x not in visited)
        # return dfs(source)

        queue = deque([source])
        visited = set([source])

        while queue:
            node = queue.popleft()

            if node == destination:
                return True

            for u in graph[node]:
                if u not in visited:
                    queue.append(u)
                    visited.add(u)

        return False


if __name__ == "__main__":
    assert Solution().validPath(
        3, [[0, 1], [1, 2], [2, 0]], 0, 2
    )
    assert not Solution().validPath(
        6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5
    )
    assert Solution().validPath(10, [
        [0, 7], [0, 8], [6, 1], [2, 0], [0, 4],
        [5, 8], [4, 7], [1, 3], [3, 5], [6, 5]
    ], 7, 5)
