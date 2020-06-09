class Solution:
    def firstUniqChar(self, s: str) -> int:
        d, seen = {}, set()
        for i in range(len(s)):
            c = s[i]
            if c in seen:
                if c in d:
                    del d[c]
            else:
                d[c] = i
                seen.add(c)
        return -1 if not d else next(iter(d.items()))[1]
'''
one pass solution, set is used for case 'aaa'
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1

        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = [0, i]
            d[s[i]][0] += 1

        minHeap = []
        for key, value in d.items():
            heappush(minHeap, (value, key))

        res = -1
        while minHeap:
            value, char = heappop(minHeap)
            if value[0] == 1:
                res = value[1]
                break
        return res
