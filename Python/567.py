class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, matched, d = 0, 0, {}
        for c in s1:
            d[c] = d.get(c, 0) + 1
        for r in range(len(s2)):
            char = s2[r]
            if char in d:
                d[char] -= 1
                if d[char] == 0:
                    matched += 1
            if matched == len(d):
                return True
            if r - l + 1 == len(s1):
                leftChar = s2[l]
                if leftChar in d:
                    if d[leftChar] == 0:
                        matched -= 1
                    d[leftChar] += 1
                l += 1
        return False
