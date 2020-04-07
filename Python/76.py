class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window_start, matched, sub_start = 0, 0, 0
        min_length = len(s) + 1
        d = {}
        for c in t:
            if c not in d:
                d[c] = 0
            d[c] += 1

        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char in d:
                d[right_char] -= 1
                if d[right_char] >= 0:
                    matched += 1

            while matched == len(t):
                if min_length > window_end - window_start + 1:
                    min_length = window_end - window_start + 1
                    sub_start = window_start

                left_char = s[window_start]
                window_start += 1
                if left_char in d:
                    if d[left_char] == 0:
                        matched -= 1
                    d[left_char] += 1
        if min_length > len(s):
            return ""
        return s[sub_start: sub_start + min_length]
