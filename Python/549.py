# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(root):
            if not root:
                return 0, 0
            # post order
            left = dfs(root.left)
            right = dfs(root.right)
            # for current node
            inc, des = 1, 1
            if root.left:
                if root.val - root.left.val == 1:
                    des = left[1] + 1
                elif root.val - root.left.val == -1:
                    inc = left[0] + 1
            if root.right:
                if root.val - root.right.val == 1:
                    des = max(des, right[1] + 1)
                elif root.val - root.right.val == -1:
                    inc = max(inc, right[0] + 1)
            self.res = max(self.res, inc + des - 1)
            return inc, des
        dfs(root)
        return self.res

