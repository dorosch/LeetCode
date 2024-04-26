from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        result = []
        to_delete = set(to_delete)

        def dfs(node, is_root):
            if not node:
                return None

            is_deleted = node.val in to_delete

            if is_root and not is_deleted:
                result.append(node)

            node.left = dfs(node.left, is_deleted)
            node.right = dfs(node.right, is_deleted)

            return None if is_deleted else node

        dfs(root, True)

        return result


if __name__ == "__main__":
    root = TreeNode(
        1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3, TreeNode(6), TreeNode(7))
    )
    answer = [
        TreeNode(1, TreeNode(2, TreeNode(4))), TreeNode(6), TreeNode(7)
    ]
    assert Solution().delNodes(root, [3, 5]) == answer
