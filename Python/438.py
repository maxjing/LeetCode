class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d = {}
        l, matched, res = 0, 0, []
        for c in p:
            d[c] = d.get(c, 0) + 1
        for r in range(len(s)):
            rightChar = s[r]
            if rightChar in d:
                d[rightChar] -= 1
                if d[rightChar] == 0:
                    matched += 1
            if matched == len(d):
                res.append(l)
            if r - l + 1 == len(p):
                leftChar = s[l]
                if leftChar in d:
                    if d[leftChar] == 0:
                        matched -= 1
                    d[leftChar] += 1
                l += 1
        return res


'''
Time: O(m + n)
'''
