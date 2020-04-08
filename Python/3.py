class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        window_start, maxLen = 0, 0
        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char in d:
                window_start = max(window_start, d[right_char] + 1)
            d[right_char] = window_end
            maxLen = max(maxLen, window_end - window_start + 1)

        return maxLen


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
