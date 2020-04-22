class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        res = []
        self.dfs(word, 0, '', 0, res)
        return res

    def dfs(self, word, pos, cur, count, res):
        if pos == len(word):
            res.append(cur + str(count) if count > 0 else cur)
        else:
          # skip current word[pos]
            self.dfs(word, pos + 1, cur, count + 1, res)
          # include current word[pos] and change count back to 0
            self.dfs(word, pos + 1, cur + (str(count) if count > 0 else '') + word[pos], 0, res)
