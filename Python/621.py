class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res, maxHeap = 0, []
        for k, v in Counter(tasks).items():
            heappush(maxHeap, (-v, k))
        while maxHeap:
            count, temp = 0, []
            while count <= n:
                res += 1
                if maxHeap:
                    freq, char = heappop(maxHeap)
                    if freq + 1 < 0:
                        heappush(temp, (freq + 1, char))
                if not maxHeap and not temp:
                    break
                else:
                    count += 1
            for item in temp:
                heappush(maxHeap, item)
        return res
'''
eg. ["A","A","A","B","B","B"], 2, h [(3, a), (3, b)]

1. i = 0, time = 1, h[(3, b)], temp = [(2, a)]
2. i = 1, time = 2, h = [], temp = [(2, a), (2,b)]
3. i = 2, time = 3, h = [], temp = [(2, a), (2,b)], 
4. i = 3, time = 3, h = [(2, a), (2, b)], temp = []
5. i = 0, time = 4, h = [(2, b)], temp = [(1, a)]
6. i = 1, time = 5, h = [], temp = [(1, a), (1, b)]
7. i = 2, time = 6, h = [], temp = [(1, a), (1, b)]
8. i = 3, time = 6, h = [(1, a), (1, b)], temp = []
9. i = 0, time = 7, h = [(1, b)], temp = []
10. i = 1, time = 8, h = [], temp = [], break
'''


