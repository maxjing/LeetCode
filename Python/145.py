# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

            res.append(node.val)
        res.reverse()
        return res


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []

        def postOrder(root):
            if not root:
                return
            postOrder(root.left)
            postOrder(root.right)
            self.res.append(root.val)

        postOrder(root)
        return self.res

