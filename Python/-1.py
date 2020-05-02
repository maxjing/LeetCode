'''
Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree
Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given string is a valid sequence in such binary tree. 

We get the given string from the concatenation of an array of integers arr and the concatenation of all values of the nodes along a path results in a sequence in the given binary tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if root is None:
            return len(arr) == 0
        else:
            return self.findPath(root, arr, 0)

    def findPath(self, node, arr, index):
        if node is None:
            return False
        if index >= len(arr) or node.val != arr[index]:
            return False
        if node.left is None and node.right is None and index == len(arr) - 1:
            return True
        return self.findPath(node.left, arr, index + 1) or self.findPath(node.right, arr, index + 1)
