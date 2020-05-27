# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#O(logn)
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        diff = math.inf
        res = 0
        while root:
            if abs(root.val - target) < abs(diff):
                diff = root.val - target
                res = root.val
            if root.val == target:
                return root.val
            elif root.val < target:
                root = root.right
            else:
                root = root.left
        return res

#O(n)
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.diff = math.inf
        self.res = 0
        self.dfs(root, target)
        return self.res

    def dfs(self, root, target):
        if root is None:
            return
        self.dfs(root.left, target)
        diff = abs(root.val - target)
        if diff < self.diff:
            self.diff = diff
            self.res = root.val
        self.dfs(root.right, target)