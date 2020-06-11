# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if node is None:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        # update global diameter if use current node as the turning point(which can only use left and right)
        # notice it is the length between two nodes, so no need plus one
        self.res = max(self.res, left + right)
        # pass the longest path to parent
        return max(left, right) + 1


'''
why last + 1 lc 104
def maxDepth(self, root: TreeNode) -> int:
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
'''
