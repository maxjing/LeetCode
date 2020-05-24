class Solution:
    def alienOrder(self, words: List[str]) -> str:
        vertices = set(c for w in words for c in w)
        indegree = {v: 0 for v in vertices}
        print(indegree)
        graph = collections.defaultdict(list)
        for w0, w1 in zip(words, words[1:]):
            if w0.startswith(w1) and len(w0) > len(w1):
                return ''
            for a, b in zip(w0, w1):
                if a != b:
                    graph[a].append(b)
                    indegree[b] += 1
                    break
        q = collections.deque(u for u, i in indegree.items() if i == 0)
        topological = []
        while q:
            u = q.popleft()
            topological.append(u)
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        return ''.join(topological) if len(topological) == len(vertices) else ''