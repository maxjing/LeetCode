# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return False
        q = deque([root])
        while q[0]:
            node = q.popleft()
            q.append(node.left if node.left else None)
            q.append(node.right if node.right else None)

        while q and not q[0]:
            q.popleft()
        return not q