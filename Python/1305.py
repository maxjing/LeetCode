# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []
        self.inorder(root1, res)
        self.inorder(root2, res)
        res.sort()
        return res

    def inorder(self, root, l):
        if not root:
            return
        self.inorder(root.left, l)
        l.append(root.val)
        self.inorder(root.right, l)
        return l
