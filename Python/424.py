class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, res, maxRepeat = 0, 0, 0
        d = {}
        for r in range(len(s)):
            rightChar = s[r]
            d[rightChar] = d.get(rightChar, 0) + 1
            maxRepeat = max(maxRepeat, d[rightChar])

            while r - l + 1 - maxRepeat > k:
                leftChar = s[l]
                d[leftChar] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
