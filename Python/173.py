# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.l = []
        self.inorder(root)
        self.count = 0

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        self.l.append(root.val)
        self.inorder(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        n = self.l[self.count]
        self.count += 1
        return n

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.count < len(self.l)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()