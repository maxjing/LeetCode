class Solution:
    def romanToInt(self, s: str) -> int:
        d = defaultdict(dict)
        d['I'] = 1
        d['V'] = 5
        d['X'] = 10
        d['L'] = 50
        d['C'] = 100
        d['D'] = 500
        d['M'] = 1000
        if not s:
            return 0
        if len(s) == 1:
            return d[s]
        res = d[s[-1]]
        for i in range(len(s) - 2, -1, -1):
            if d[s[i]] < d[s[i + 1]]:
                res -= d[s[i]]
            else:
                res += d[s[i]]
        return res

