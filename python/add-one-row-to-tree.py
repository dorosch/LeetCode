from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if depth == 1:
            return TreeNode(val, root)

        def dfs(node: Optional[TreeNode], level: int):
            if not node:
                return

            if level == depth - 1:
                node.left = TreeNode(val, left=node.left)
                node.right = TreeNode(val, right=node.right)

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 1)

        return root
