class Solution:
    def canFinish(self, numCourses: int, p: List[List[int]]) -> bool:
        if numCourses < 0:
            return False
        inDegree = [0] * numCourses
        for x, y in p:
            inDegree[x] += 1
        q = deque()
        for i, v in enumerate(inDegree):
            if v == 0:
                q.append(i)
        while q:
            start = q.popleft()
            for x, y in p:
                if y == start:
                    inDegree[x] -= 1
                    if inDegree[x] == 0:
                        q.append(x)

        for x in inDegree:
            if x != 0:
                return False
        return True