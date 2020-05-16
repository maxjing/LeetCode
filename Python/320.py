# 2020.05.16 new version better to understand
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        res = []
        self.dfs(word, 0, "", 0, res)
        return res

    def dfs(self, word, pos, cur, count, res):
        if pos == len(word):
            if count > 0:
                res.append(cur + str(count))
            else:
                res.append(cur)

        else:
           # skip current word[pos]
            self.dfs(word, pos + 1, cur, count + 1, res)
            # include current word[pos] and change count back to 0
            if count > 0:
                self.dfs(word, pos + 1, cur + str(count) + word[pos], 0, res)
            else:
                self.dfs(word, pos + 1, cur + word[pos], 0, res)
