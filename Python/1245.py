class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(set)

        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)

        self.start = [0, None]

        def dfs(s):
            seen = {s}
            stack = [(s, 0)]
            while stack:
                u, d = stack.pop()
                if d > self.start[0]:
                    self.start = [d, u]

                for v in graph[u]:
                    if v not in seen:
                        seen.add(v)
                        stack.append((v, d + 1))

        dfs(edges[0][0])
        dfs(self.start[1])

        return self.start[0]