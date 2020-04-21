# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        return self.countPathSum(root, sum, [])

    def countPathSum(self, node, sum, currentPath):
        if node is None:
            return 0
        currentPath.append(node.val)
        pathCount, pathSum = 0, 0
        for i in range(len(currentPath) - 1, -1, -1):
            pathSum += currentPath[i]
            if pathSum == sum:
                pathCount += 1

        pathCount += self.countPathSum(node.left, sum, currentPath)
        pathCount += self.countPathSum(node.right, sum, currentPath)

        del currentPath[-1]

        return pathCount
