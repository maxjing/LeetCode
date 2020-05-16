# bfs
# 2020.05.16 forgot to do


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        res.append(S)
        for i in range(len(S)):
            if S[i].isalpha():
                for j in range(len(res)):
                    subset = list(res[j])
                    subset[i] = subset[i].swapcase()
                    res.append("".join(subset))
        return res
