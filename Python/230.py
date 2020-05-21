# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        count = 0
        res = 0
        while stack or root is not None:
            while root is not None:
                stack.append(root)
                root = root.left

            root = stack.pop()
            count += 1
            if count == k:
                res = root.val
                break
            root = root.right
        return res