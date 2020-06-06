class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['#', 0]]
        for c in s:
            if c == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return "".join(c * n for c, n in stack)

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if len(s) == 1:
            return s
        size = -1
        while size != len(s):
            size = len(s)
            for i in range(len(s)):
                if i == 0 or s[i] != s[i - 1]:
                    count = 1
                else:
                    count += 1
                    if count == k:
                        s = s[:i - k + 1] + s[i + 1:]
                        break
        return s



