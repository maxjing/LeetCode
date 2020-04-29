class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, res = 0, 0
        d = {}
        for r in range(len(s)):
            char = s[r]
            if char in d:
                l = max(d[char] + 1, l)
            d[char] = r
            res = max(res, r - l + 1)
        return res


'''why need maxmize window_start
abba
1. d = {a : 0}, start = 0
2. d = {a: 0, b : 1}, start = 0
3. d = {a: 0, b : 2}, start = max(0, d[b] + 1) = max(0, 2) = 2
4. d = {a: 3, b : 2}
without max: start = d[a] + 1 = 1
with max: start = max(2, d[a] + 1) = 2
choose the right a not the previous a
'''
