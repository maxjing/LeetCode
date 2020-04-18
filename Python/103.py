# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = deque()
        if root is None:
            return res
        q = deque()
        q.append(root)
        count = -1
        while q:
            count += 1
            size = len(q)
            l = []
            for _ in range(size):
                node = q.popleft()
                l.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            if count % 2 != 0:
                l.reverse()
            res.append(l)
        return res
