class Solution:
    def convertToTitle(self, n: int) -> str:
        t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        d = {}
        for i, v in enumerate(t):
            d[i] = v
        res = []
        while n > 0:
            res.append(d[(n - 1) % 26])
            n = (n-1) // 26
        res.reverse()
        return "".join(res)