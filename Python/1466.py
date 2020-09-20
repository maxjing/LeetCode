# bfs
class Solution:
    def minReorder(self, n: int, graph: List[List[int]]) -> int:
        d = defaultdict(list)
        paths = set()
        for u, v in graph:
            d[u].append(v)
            d[v].append(u)
            paths.add((u, v))

        visited = [False for _ in range(n)]
        q = deque()
        q.append([0, -1])
        res = 0
        while q:
            u, v = q.popleft()
            if visited[u]:
                continue
            visited[u] = True
            # 相反的direction
            if (v, u) in paths:
                res += 1
            for nei in d[u]:
                if not visited[nei]:
                    q.append((nei, u))
        return res


# dfs
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.res = 0
        paths = set([0])
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
            paths.add((u, v))

        def dfs(node, parent):
            if (parent, node) in paths:
                self.res += 1
            for v in graph[node]:
                # means visited, already processed its parent
                if v != parent:
                    dfs(v, node)

        dfs(0, -1)
        return self.res


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.res = 0
        paths = set([0])
        graph = defaultdict(list)
        self.visited = set()
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
            paths.add((u, v))

        def dfs(u, parent):
            if u in self.visited:
                return
            self.visited.add(u)
            if (parent, u) in paths:
                self.res += 1
            for v in graph[u]:
                if v not in self.visited:
                    dfs(v, u)

        dfs(0, -1)
        return self.res
