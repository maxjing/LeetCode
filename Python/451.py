# heap
class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1

        maxHeap = []
        for key, value in d.items():
            heappush(maxHeap, (-value, key))
        res = []
        while maxHeap:
            freq, char = heappop(maxHeap)
            for _ in range(-freq):
                res.append(char)
        return "".join(res)

# hashmap


class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1

        res = []
        for key, value in sorted(d.items(), key=lambda x: x[1], reverse=True):
            for _ in range(value):
                res.append(key)
        return "".join(res)
