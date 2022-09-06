class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levels = []

        def traversal(node, level):
            if node:
                if level < len(levels):
                    levels[level] += node.val
                else:
                    levels.append(node.val)

                traversal(node.left, level + 1)
                traversal(node.right, level + 1)

        traversal(root, 0)

        return levels.index(max(levels)) + 1
