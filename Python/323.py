#bfs
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = {x: [] for x in range(n)}
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        res = 0
        for i in range(n):
            q = [i]
            if i in g:
                res += 1
            for j in q:
                if j in g:
                    q += g[j]
                    del g[j]
        return res

'''
O(n+m)
'''