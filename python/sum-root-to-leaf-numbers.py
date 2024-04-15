from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.leafNumbers(root, 0)

    def leafNumbers(self, node: Optional[TreeNode], value: int) -> List[int]:
        if not node:
            return 0

        value = value * 10 + node.val

        if not node.left and not node.right:
            return value

        return (
            self.leafNumbers(node.left, value) +
            self.leafNumbers(node.right, value)
        )


if __name__ == "__main__":
    assert Solution().sumNumbers(TreeNode(9)) == 9
    assert Solution().sumNumbers(TreeNode(1, TreeNode(2), TreeNode(3))) == 25
    assert Solution().sumNumbers(
        TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
    ) == 1026
