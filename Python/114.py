# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None

        def dfs(root):
            if not root:
                return None
            dfs(root.right)
            dfs(root.left)
            root.right = self.prev
            root.left = None
            self.prev = root

        dfs(root)

'''
先到最右边最后一个， right 接上前一个 ，left 为空
'''