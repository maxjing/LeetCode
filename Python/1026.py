# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#dfs
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.res = -math.inf
        self.dfs(root, root.val, root.val)
        return self.res

    def dfs(self, root, mn, mx):
        if not root:
            return
        if root.val > mx:
            mx = root.val
            self.res = max(self.res, abs(mx - mn))
        if root.val < mn:
            mn = root.val
            self.res = max(self.res, abs(mx - mn))
        self.dfs(root.left, mn, mx)
        self.dfs(root.right, mn, mx)


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = [(root, root.val, root.val)]
        ans = 0
        while queue:
            node, minval, maxval = queue.pop(0)

            if node is None:
                ans = max(abs(minval - maxval), ans)
                continue
            minval = min(minval, node.val)
            maxval = max(maxval, node.val)

            queue.append((node.left, minval, maxval))
            queue.append((node.right, minval, maxval))
        return ans