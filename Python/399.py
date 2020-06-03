class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(dict)
        for i in range(len(equations)):
            equation = equations[i]
            value = values[i]
            g[equation[0]][equation[1]] = value
            g[equation[1]][equation[0]] = 1 / value

        def dfs(g, start, end, visited):
            visited.add(start)
            for n in g[start]:
                if n == end:
                    return g[start][n]
                elif n not in visited:
                    ans = dfs(g, n, end, visited)
                    if ans != -1:
                        #update graph
                        g[n][end] = ans
                        return g[start][n] * ans
            return -1

        res = []
        for start, end in queries:
            if start not in g and end not in g:
                res.append(-1.0)
            elif start in g and end == start:
                res.append(1.0)
            elif end in g[start]:
                res.append(g[start][end])
            else:
                visited = set()
                ans = dfs(g, start, end, visited)
                res.append(ans)
        return res