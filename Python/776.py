# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: TreeNode, V: int) -> List[TreeNode]:
        if not root:
            return [None, None]
        if root.val > V:
            l,r = self.splitBST(root.left, V)
            root.left = r
            return [l, root]
        else:
            l,r = self.splitBST(root.right, V)
            root.right = l
            return [root, r]

'''
https://leetcode.com/problems/split-bst/discuss/159985/Python-DFS-tm
'''