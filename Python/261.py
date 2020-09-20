class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0 or len(edges) != n - 1:
            return False

        d = defaultdict(list)
        for x, y in edges:
            d[x].append(y)
            d[y].append(x)
        set_, q = set([0]), deque([0])
        while q:
            node = q.popleft()
            for nei in d[node]:
                if nei not in set_:
                    set_.add(nei)
                    q.append(nei)
        return len(set_) == n
