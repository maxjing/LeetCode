class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            return s
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        maxHeap = []
        for key, value in d.items():
            heappush(maxHeap, (-value, key))
        res = []
        q = deque()
        while maxHeap:
            freq, char = heappop(maxHeap)
            res.append(char)
            #2020.05.18 just add to q everytime, and check when len(q) == k
            q.append((char, freq + 1))
            if len(q) == k:
                char, freq = q.popleft()
                if -freq > 0:
                    heappush(maxHeap, (freq, char))
        return "".join(res) if len(res) == len(s) else ""
