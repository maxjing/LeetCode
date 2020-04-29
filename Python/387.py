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
