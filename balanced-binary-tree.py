from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def isSubtreeBalanced(node):
            if not node:
                return True, 0

            is_left_subtree_balanced, left_node_depth = isSubtreeBalanced(
                node.left
            )
            is_right_subtree_balanced, right_node_depth = isSubtreeBalanced(
                node.right
            )

            return (
                is_left_subtree_balanced and
                is_right_subtree_balanced and
                abs(left_node_depth - right_node_depth) <= 1,
                max(left_node_depth, right_node_depth) + 1
            )

        return isSubtreeBalanced(root)[0] if root else True


if __name__ == '__main__':
    assert Solution().isBalanced(None)
