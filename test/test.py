from collections import *
from typing import *


class Solution:
    def minReorder(self, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set([0])
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        connections = set(map(tuple, connections))
        queue = deque([0])
        changes = 0
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if v not in visited:
                    if (u, v) in connections:
                        changes += 1
                    queue.append(v)
                    visited.add(v)
        return changes

    def main(self):

        res = self.minReorder([[0,1],[1,3],[2,3],[4,0],[4,5]])
        print(res)


if __name__ == '__main__':
    d = Solution()
    d.main()