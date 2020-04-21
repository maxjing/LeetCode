# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.treeDiameter = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.calculate_height(root)
        return self.treeDiameter

    def calculate_height(self, node):
        if node is None:
            return 0

        leftTreeHeight = self.calculate_height(node.left)
        rightTreeHeight = self.calculate_height(node.right)

        diameter = leftTreeHeight + rightTreeHeight
        # update global diameter if use current node as the turning point(which can only use left and right)
        self.treeDiameter = max(self.treeDiameter, diameter)
        # pass the longest path to parent
        return max(leftTreeHeight, rightTreeHeight) + 1


'''
why last + 1 lc 104
def maxDepth(self, root: TreeNode) -> int:
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
'''
