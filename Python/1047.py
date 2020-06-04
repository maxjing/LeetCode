class Solution:
    def removeDuplicates(self, S: str) -> str:
        res = []
        for c in S:
            if res and res[-1] == c:
                res.pop()
            else:
                res.append(c)
        return "".join(res)
#this one is slow
class Solution:
    def removeDuplicates(self, S: str) -> str:
        def dfs(s):
            for i in range(len(s) - 1):
                if s[i + 1] == s[i]:
                    return dfs(s[0:i] + s[i + 2:])
            return s
        return dfs(S)
