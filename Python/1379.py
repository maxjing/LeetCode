# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def dfs(original, cloned, target):
            if original:
                if original.val == target.val:
                    return cloned
                else:
                    return dfs(original.left, cloned.left, target) or dfs(original.right, cloned.right, target)
        return dfs(original, cloned, target)
