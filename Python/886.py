class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for x, y in dislikes:
            graph[x].append(y)
            graph[y].append(x)
        partition = [0] * (N + 1)
        for i in range(1, N + 1):
            if partition[i] == 0:
                partition[i] = 1
                q = deque()
                q.append(i)
                while q:
                    idx = q.popleft()
                    for node in graph[idx]:
                        if partition[node] == partition[idx]:
                            return False
                        elif partition[node] == 0:
                            partition[node] = -partition[idx]
                            q.append(node)
        return True

