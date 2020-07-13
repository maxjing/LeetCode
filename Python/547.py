class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        visited = set()
        def dfs(r):
            for i, v in enumerate(M[r]):
                if v == 1 and i not in visited:
                    visited.add(i)
                    dfs(i)
        count = 0
        for i in range(len(M)):
            if i not in visited:
                count += 1
                dfs(i)
        return count

'''
O(n^2)
'''