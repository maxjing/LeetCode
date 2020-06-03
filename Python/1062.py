class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        l, curr_size, res = 0, 0, 0
        for r in range(len(s)):
            sub = s[l:r + 1]
            if sub in s[l + 1:]:
                curr_size += 1
                r += 1
                res = max(res, curr_size)
            elif l == r:
                r += 1
                l += 1
            else:
                l += 1
        return res

