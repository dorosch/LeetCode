class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        def subtreeSum(node: Optional[TreeNode], value) -> int:
            if not node:
                return 0

            return value + subtreeSum(node.left, node.val) + subtreeSum(node.right, node.val)

        return root.val == (subtreeSum(root.left, root.left.val) + subtreeSum(root.right, root.right.val))
