class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l, maxLen = 0, 0
        d = {}
        for r in range(len(s)):
            rightChar = s[r]
            d[rightChar] = d.get(rightChar, 0) + 1
            while len(d) > k:
                leftChar = s[l]
                d[leftChar] -= 1
                if d[leftChar] == 0:
                    del d[leftChar]
                l += 1
            maxLen = max(maxLen, r - l + 1)
        return maxLen
