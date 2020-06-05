# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        return self.dfs(root, k, set())

    def dfs(self, node, k, set_):
        if not node:
            return False
        if k - node.val in set_:
            return True
        set_.add(node.val)
        return self.dfs(node.left, k, set_) or self.dfs(node.right, k, set_)
