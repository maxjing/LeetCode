# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root is None:
            return False
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            isX = False
            isY = False
            for _ in range(size):
                node = q.popleft()
                #2020.05.14 check node.val first and set flag, node child just check not need set flag
                if node.val == x:
                    isX = True
                if node.val == y:
                    isY = True
                if node.left is not None and node.right is not None:
                    if node.left.val == x and node.right.val == y:
                        return False
                    if node.left.val == y and node.right.val == x:
                        return False
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            if isX and isY:
                return True
        return False


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        res = []
        self.dfs(root, None, 0, x, y, res)
        return res[0][0] != res[1][0] and res[0][1] == res[1][1]

    def dfs(self, node, parent, depth, x, y, res):
        if node is None or len(res) == 2:
            return
        if node.val == x or node.val == y:
            res.append([parent, depth])
        self.dfs(node.left, node, depth + 1, x, y, res)
        self.dfs(node.right, node, depth + 1, x, y, res)
