# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(root):
            if not root:
                return math.inf, -math.inf, 0
            lmin, lmax, lsize = dfs(root.left)
            rmin, rmax, rsize = dfs(root.right)

            n = -math.inf
            if root.val > lmax and root.val < rmin:
                n = lsize + rsize + 1
                self.res = max(self.res, n)

            return min(root.val, lmin), max(root.val, rmax), n
        dfs(root)
        return self.res
