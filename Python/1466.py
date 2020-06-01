# bfs
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        visited = set([0])
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        connections = set(map(tuple, connections))
        queue = collections.deque([0])
        changes = 0
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if v in visited:
                    continue
                visited.add(v)
                if (u, v) in connections:
                    changes += 1
                queue.append(v)
        return changes

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
                #means visited, already processed its parent
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