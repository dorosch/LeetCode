from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root:
            if root.val == val:
                return root

            return self.searchBST(root.left, val) or self.searchBST(root.right, val)


if __name__ == '__main__':
    assert Solution().searchBST(
        TreeNode(1, TreeNode(2), TreeNode(3)), 2
    ).val == 2
