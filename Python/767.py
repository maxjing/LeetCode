class Solution:
    def reorganizeString(self, S: str) -> str:
        d = {}
        for c in S:
            d[c] = d.get(c, 0) + 1
        res = []
        maxHeap = []
        for key, value in d.items():
            heappush(maxHeap, (-value, key))
        res = []
        prevChar, prevFreq = None, 0
        while maxHeap:
            freq, char = heappop(maxHeap)
            if prevChar and -prevFreq > 0:
                heappush(maxHeap, (prevFreq, prevChar))
            res.append(char)
            prevChar = char
            prevFreq = freq + 1
        return "".join(res) if len(res) == len(S) else ""


'''
Time: O(nlogn)
'''
