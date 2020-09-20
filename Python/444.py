class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        values = {x for seq in seqs for x in seq}
        d = {x: [] for x in values}
        inDegree = {x: 0 for x in values}

        for seq in seqs:
            for i in range(len(seq) - 1):
                x = seq[i]
                y = seq[i+1]
                inDegree[y] += 1
                d[x].append(y)

        # get start node
        q = deque()
        for node, count in inDegree.items():
            if count == 0:
                q.append(node)
        if len(q) > 1:
            return False
        print(d)
        # bfs
        res = []
        while q:
            if len(q) != 1:
                return False
            node = q.popleft()
            res.append(node)
            for nei in d[node]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    q.append(nei)
      # 2020.08.30 notice here len(values) not len(org), has to connect each element in seq
        return len(res) == len(values) and res == org
