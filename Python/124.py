# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        #initial with -math.inf not 0 2020.05.30
        self.globalMaximum = -math.inf
        self.findMaxPathSum(root)
        return self.globalMaximum

    def findMaxPathSum(self, node):
        if node is None:
            return 0
         # ignore any path which has an overall negative sum.
        leftMaximum = max(self.findMaxPathSum(node.left), 0)
        rightMaximum = max(self.findMaxPathSum(node.right), 0)
        # if use current node as the start node for the path
        localMaximum = leftMaximum + rightMaximum + node.val
        self.globalMaximum = max(self.globalMaximum, localMaximum)
        # pass the maximum path to the parent
        return max(leftMaximum, rightMaximum) + node.val
