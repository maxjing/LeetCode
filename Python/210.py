# bfs
class Solution:
    def findOrder(self, numCourses: int, pre: List[List[int]]) -> List[int]:
        # get indegree
        inDegree = [0] * numCourses
        for x, y in pre:
            inDegree[x] += 1

        # get startNodes
        q = deque()
        for i, v in enumerate(inDegree):
            if v == 0:
                q.append(i)

        # bfs
        if len(q) == 0:
            return []
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for x, y in pre:
                if y == node:
                    inDegree[x] -= 1
                    if inDegree[x] == 0:
                        q.append(x)
        return res if len(res) == numCourses else []


class Solution:

    def findOrder(self, n: int, p: List[List[int]]) -> List[int]:
        in_ = [0] * n
        for x, _ in p:
            in_[x] += 1
        q = deque()
        for i, v in enumerate(in_):
            if v == 0:
                q.append(i)
        res, count = [], 0
        while q:
            start = q.popleft()
            count += 1
            res.append(start)
            for x, y in p:
                if y == start:
                    in_[x] -= 1
                    if in_[x] == 0:
                        q.append(x)

        return res if count == n else []


'''
smilar to 207, O(v+e)
'''


# dfs
class Solution:
    def findOrder(self, numCourses, prerequisites):
        dic = defaultdict(set)
        neigh = defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        stack = [i for i in range(numCourses) if not dic[i]]
        res = []
        while stack:
            node = stack.pop()
            res.append(node)
            for i in neigh[node]:
                # prerequisite satisfy
                dic[i].remove(node)
                if not dic[i]:
                    stack.append(i)
            dic.pop(node)
        return res if not dic else []
