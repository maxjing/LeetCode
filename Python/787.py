class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        d = defaultdict(dict)
        for u, v, w in flights:
            d[u][v] = w
        heap = [(0, src, K+1)]
        while heap:
            p, i, k = heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in d[i]:
                    heappush(heap, (p + d[i][j], j, k - 1))
        return -1