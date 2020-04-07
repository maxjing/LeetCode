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
