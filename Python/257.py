# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        self.findAllPaths(root, [], paths)
        return paths

    def findAllPaths(self, node, currentPath, paths):
        if node is None:
            return
        currentPath.append(str(node.val))
        if node.left is None and node.right is None:
            paths.append("->".join(currentPath))
        else:
            self.findAllPaths(node.left, currentPath, paths)
            self.findAllPaths(node.right, currentPath, paths)
        del currentPath[-1]
