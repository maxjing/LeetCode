# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.ans = 0
        self.dfs(root, L, R)
        return self.ans

    def dfs(self, node, L, R):
        if node:
            if L <= node.val <= R:
                self.ans += node.val
            # after added, check go which direction
            # go smaller
            if L < node.val:
                self.dfs(node.left, L, R)
            # go bigger
            if node.val < R:
                self.dfs(node.right, L, R)

# 2020.05.25 inorder traverse


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.res = []
        self.inorderRec(root)
        sum = 0
        for n in self.res:
            if n >= L and n <= R:
                sum += n
        return sum

    def inorderRec(self, root):
        if root is None:
            return
        self.inorderRec(root.left)
        self.res.append(root.val)
        self.inorderRec(root.right)
