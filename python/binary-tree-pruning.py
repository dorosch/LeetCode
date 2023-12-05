class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left = self.pruneTree(root.left)
            root.right = self.pruneTree(root.right)
      
            return root if root.left or root.right or root.val == 1 else None
