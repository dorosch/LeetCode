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
