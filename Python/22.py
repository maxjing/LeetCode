# dfs
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs(res, "", 0, 0, n)
        return res

    def dfs(self, res, s, open, close, max):
        if len(s) == max * 2:
            res.append(s)
        if open < max:
            self.dfs(res,  s + '(', open + 1, close, max)
        if close < open:
            self.dfs(res, s + ')', open, close + 1, max)
