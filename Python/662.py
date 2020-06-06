# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:

        res = 0
        if not root:
            return res

        deq = deque()
        deq.append([(root, 1)])

        while deq:
            level = deq.popleft()
            next_level = []

            res = max(res, level[-1][1] - level[0][1] + 1)

            for node, depth in level:
                if node.left:
                    next_level.append((node.left, 2 * depth))
                if node.right:
                    next_level.append((node.right, 2 * depth + 1))

            if next_level:
                deq.append(next_level)

        return res