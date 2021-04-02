class Solution:
    def reorganizeString(self, S: str) -> str:
        d = {}
        for c in S:
            d[c] = d.get(c, 0) + 1
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
'aaab'
1. maxHeap = [(3, a), (1, b)], prevChar = None, prevFreq = 0, res = []
2. maxHeap = [(1, b)], char = a, freq = 3, res = ['a'], prevChar = a, prevFreq = 2
3. maxHeap = [], char = b, freq = 1, res = ['a', 'b'], 
maxHeap = [(2, 'a')], prevChar = 0, prevChar = b,
4. maxHeap maxHeap = [], char = a, freq = 2, res = ['a', 'b', 'a'], no heappush because b = 0
'''
'''
Time: O(nlogn)
'''
