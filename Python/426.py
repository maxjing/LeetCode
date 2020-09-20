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
        res = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root)
            inorder(root.right)
        inorder(root)

        for i, node in enumerate(res):
            # 先看这个条件 在看 == 0 e.g.[1]
            if i == len(res) - 1:
                node.left = res[i-1]
                node.right = res[0]
            elif i == 0:

                node.left = res[-1]
                node.right = res[i+1]

            else:
                node.left = res[i-1]
                node.right = res[i+1]
        return res[0] if res else None


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
        # 2020.05.31 [4,2,1,3,5], dummy.right -> 1, prev -> 5, 需要返回loop,把他们俩接起来， 1 no preaccesor, 5 no successor
        dummy.right.left, prev.right = prev, dummy.right
        return dummy.right
