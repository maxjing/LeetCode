class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = 0
        for c in s:
            if c == '(' or c == '*':
                stack += 1
            else:
                stack -= 1
                if stack < 0:
                    return False
        reversedStack = 0
        for c in reversed(s):
            if c == ')' or c == '*':
                reversedStack += 1
            else:
                reversedStack -= 1
                if reversedStack < 0:
                    return False
        return True


