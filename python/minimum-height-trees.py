from typing import List
from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(set)

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        leaves = [i for i in range(n) if len(graph[i]) == 1]

        while n > 2:
            new_leaves = []
            n -= len(leaves)

            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves


if __name__ == "__main__":
    assert Solution().findMinHeightTrees(
        4, [[1, 0], [1, 2], [1, 3]]
    ) == [1]
    assert Solution().findMinHeightTrees(
        6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
    ) == [3, 4]
