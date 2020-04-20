# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.pathsSum(root, 0)

    def pathsSum(self, node, pathSum):
        if node is None:
            return 0
        pathSum = 10 * pathSum + node.val

        if node.left is None and node.right is None:
            return pathSum

        return self.pathsSum(node.left, pathSum) + self.pathsSum(node.right, pathSum)
