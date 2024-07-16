from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        nodes = dict()
        parents = dict()
        childs = defaultdict(list)
        visited = set()
        stack = [(startValue, "")]

        def dfs(node: Optional[TreeNode]):
            if not node:
                return

            nodes[node.val] = node

            if node.left:
                parents[node.left.val] = node.val
                childs[node.val].append(node.left.val)
                dfs(node.left)

            if node.right:
                parents[node.right.val] = node.val
                childs[node.val].append(node.right.val)
                dfs(node.right)

        dfs(root)

        while stack:
            value, path = stack.pop()

            if value == destValue:
                return path

            if value in visited:
                continue

            visited.add(value)

            if value in parents:
                stack.append((parents[value], path + "U"))

            if value in childs:
                for child in childs[value]:
                    if child in visited:
                        continue

                    node = nodes[value]

                    if node.left and node.left.val == child:
                        stack.append((child, path + "L"))
                    else:
                        stack.append((child, path + "R"))

        return ""


if __name__ == "__main__":
    assert Solution().getDirections(TreeNode(2, TreeNode(1)), 2, 1) == "L"
    assert Solution().getDirections(
        TreeNode(5, TreeNode(1, TreeNode(3)), TreeNode(2, TreeNode(6), TreeNode(4))),
        3, 6
    ) == "UURL"
