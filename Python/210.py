class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = {i: set() for i in range(numCourses)}
        nei = defaultdict(set)
        for x, y in prerequisites:
            d[x].add(y)
            nei[y].add(x)
        q = deque([i for i in d if not d[i]])
        count, res = 0, []
        while q:
            node = q.popleft()
            count += 1
            res.append(node)
            for i in nei[node]:
                d[i].remove(node)
                if not d[i]:
                    q.append(i)
        return res if count == numCourses else []


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
