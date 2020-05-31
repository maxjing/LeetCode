# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        return self.dfs(root)[1]

    def dfs(self, root):
        if not root:
            return 0, None

        d1, h1 = self.dfs(root.left)
        d2, h2 = self.dfs(root.right)
        if d1 > d2:
            return d1 + 1, h1
        elif d1 < d2:
            return d2 + 1, h2
        return d1 + 1, root
