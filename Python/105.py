# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder and not inorder:
            return None
        self.root_idx = 0
        d = defaultdict(dict)
        for i, v in enumerate(inorder):
            d[v] = i

        def helper(l, r):
            if l > r:
                return
            root = TreeNode(preorder[self.root_idx])
            pos = d[preorder[self.root_idx]]
            self.root_idx += 1
            root.left = helper(l, pos - 1)
            root.right = helper(pos + 1, r)

            return root

        return helper(0, len(inorder) - 1)


'''
preorder decide the root order
the root value split inorder into left and right subtree
'''