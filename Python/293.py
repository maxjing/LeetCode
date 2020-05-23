class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        if "++" not in s:
            return []
        res = []
        for i in range(1, len(s)):
            if s[i] == '+' and s[i - 1] == '+':
                l = list(s)
                l[i] = '-'
                l[i - 1] = '-'
                res.append("".join(l))

        return res

