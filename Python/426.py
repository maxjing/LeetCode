"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return
        stack = []
        dummy = Node(0, None, None)
        prev = dummy
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            root.left, prev.right, prev = prev, root, root
            root = root.right
        #2020.05.31 [4,2,1,3,5], dummy.right -> 1, prev -> 5, 需要返回loop,把他们俩接起来， 1 no preaccesor, 5 no successor
        dummy.right.left, prev.right = prev, dummy.right
        return dummy.right


