class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window_start, matched = 0, 0
        d = {}
        for c in p:
            if c not in d:
                d[c] = 0
            d[c] += 1
        res = []
        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char in d:
                d[right_char] -= 1
                if d[right_char] == 0:
                    matched += 1

            if matched == len(d):
                res.append(window_start)

            if window_end >= len(p) - 1:
                left_char = s[window_start]
                window_start += 1
                if left_char in d:
                    if d[left_char] == 0:
                        matched -= 1
                    d[left_char] += 1
        return res
