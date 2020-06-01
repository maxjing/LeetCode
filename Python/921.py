class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        res = 0
        for c in S:
            if c == '(':
                stack.append(c)
            if c == ')':
                if not stack:
                    res += 1
                else:
                    stack.pop()
        return res + len(stack)

'''
stack will left not complete (, res counts missing ), so add them up
'''