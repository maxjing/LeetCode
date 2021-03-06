# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root is None:
            return []
        res = []
        self.dfs(root, sum, [], res)
        return res

    def dfs(self, node, sum, sublist, res):
        if node is None:
            return
        if node.left is None and node.right is None and node.val == sum:
            sublist.append(node.val)
            res.append(sublist)
        else:
            self.dfs(node.left, sum - node.val, sublist + [node.val], res)
            self.dfs(node.right, sum - node.val, sublist + [node.val], res)


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        allPaths = []
        self.findPathSum(root, sum, [], allPaths)
        return allPaths

    def findPathSum(self, node, target, currentPath, allPaths):
        if node is None:
            return
        currentPath.append(node.val)
        if node.val == target and node.left is None and node.right is None:
            allPaths.append(list(currentPath))
        else:
            self.findPathSum(node.left, target - node.val, currentPath, allPaths)
            self.findPathSum(node.right, target - node.val, currentPath, allPaths)
        del currentPath[-1]


'''
 Time: O(N^2), where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once (which will take O(N), and for every leaf node we might have to store its path which will take O(N).
'''
