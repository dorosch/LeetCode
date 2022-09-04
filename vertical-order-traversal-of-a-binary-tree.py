class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        positions = defaultdict(lambda: defaultdict(list))

        def traversal(node: Optional[TreeNode], row: int, col: int):
            if node:
                positions[col][row].append(node.val)

                if node.left:
                    traversal(node.left, row + 1, col - 1)

                if node.right:
                    traversal(node.right, row + 1, col + 1)

        traversal(root, 0, 0)

        return [
            itertools.chain.from_iterable([
                sorted(positions[column][row]) for row in sorted(positions[column].keys())
            ])
            for column in sorted(positions.keys())
        ]
