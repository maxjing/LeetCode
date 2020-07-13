# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n <= 0:
            return []

        def generate(l, r):
            if l > r:
                return [None]

            res = []
            for i in range(l, r + 1):
                l_trees = generate(l, i - 1)
                r_trees = generate(i + 1, r)
                for left in l_trees:
                    for right in r_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        res.append(root)
            return res

        return generate(1, n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n <= 0:
            return []

        def dfs(l, r):
            if l == r:
                return [None]
            res = []
            for i in range(l, r):
                l_trees = dfs(l, i)
                r_trees = dfs(i + 1, r)
                for left in l_trees:
                    for right in r_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        res.append(root)
            return res
        return dfs(1, n+1)
'''
l == r means not including n+1 when l == n+1 break
l > r means including n+1 when l == n+1
'''