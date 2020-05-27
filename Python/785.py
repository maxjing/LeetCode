class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        partition = [0] * n
        for i in range(n):
            if partition[i] == 0:
                q = deque([i])
                partition[i] = 1
                while q:
                    f = q.popleft()
                    for neighbor in graph[f]:
                        if partition[neighbor] == partition[f]:
                            return False
                        elif partition[neighbor] == 0:
                            partition[neighbor] = -partition[f]
                            q.append(neighbor)

        return True

'''
Our goal is trying to use two colors to color the graph and see if there are any adjacent nodes having the same color.
Initialize a color[] array for each node. Here are three states for colors[] array:
0: Haven't been colored yet.
1: Blue.
-1: Red.
For each node,

    If it hasn't been colored, use a color to color it. Then use the other color to color all its adjacent nodes (DFS).
    If it has been colored, check if the current color is the same as the color that is going to be used to color it. (Please forgive my english... Hope you can understand it.)

'''
