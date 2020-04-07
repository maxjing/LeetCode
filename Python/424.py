class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        max_len, window_start, max_repeat = 0, 0, 0
        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char not in d:
                d[right_char] = 0
            d[right_char] += 1
            max_repeat = max(max_repeat, d[right_char])
            while(window_end - window_start + 1 - max_repeat > k):
                left_char = s[window_start]
                d[left_char] -= 1
                window_start += 1
            max_len = max(max_len, window_end - window_start + 1)
        return max_len
