# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n <= 0:
            return []

        def generate(l, r):
            if l > r:
                return [None]

            result = []
            for i in range(l, r + 1):
                l_trees = generate(l, i - 1)
                r_trees = generate(i + 1, r)
                for left in l_trees:
                    for right in r_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        result.append(root)
            return result

        return generate(1, n)