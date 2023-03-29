from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            if node:
                return inorder(node.left) + [node.val] + inorder(node.right)

            return []

        return inorder(root)[k - 1]


if __name__ == '__main__':
    assert Solution().kthSmallest(
        TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4)), 1
    ) == 1
    assert Solution().kthSmallest(
        TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6)), 3
    ) == 3
