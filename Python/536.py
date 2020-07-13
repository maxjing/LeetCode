# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        if not s:
            return None
        stack, num = [], ''
        for c in s:
            if c not in ['(', ')']:
                num += c
            else:
                # ( )
                if num:
                    stack.append(TreeNode(int(num)))
                    num = ''
                if c == ')':
                    temp = stack.pop()
                    if stack[-1].left:
                        stack[-1].right = temp
                    else:
                        stack[-1].left = temp
        # case "4" no parentheses
        if num:
            stack.append(TreeNode(int(num)))
        return stack[-1]