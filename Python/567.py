class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = {}
        window_start, matched = 0, 0
        for c in s1:
            if c not in d:
                d[c] = 0
            d[c] += 1
        for window_end in range(len(s2)):
            right_char = s2[window_end]
            if right_char in d:
                d[right_char] -= 1
                if d[right_char] == 0:
                    matched += 1
            'remember len d not len s1'
            if matched == len(d):
                return True
            if window_end >= len(s1) - 1:
                left_char = s2[window_start]
                window_start += 1
                if left_char in d:
                    if d[left_char] == 0:
                        matched -= 1
                    d[left_char] += 1
        return False
