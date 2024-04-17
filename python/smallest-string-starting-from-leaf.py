from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        results = []
        to_str = lambda prefix: "".join(chr(97 + num) for num in prefix)[::-1]

        def dfs(node: Optional[TreeNode], prefix: List[int]) -> str:
            if not node.left and not node.right:
                results.append(to_str(prefix + [node.val]))

            if node.left:
                dfs(node.left, prefix + [node.val])

            if node.right:
                dfs(node.right, prefix + [node.val])

        dfs(root, [])

        return min(results)


if __name__ == "__main__":
    assert Solution().smallestFromLeaf(TreeNode(0, right=TreeNode(1))) == "ba"
    assert Solution().smallestFromLeaf(
        TreeNode(0, TreeNode(1, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(3), TreeNode(4)))
    ) == "dba"
    assert Solution().smallestFromLeaf(
        TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    ) == "hud"
