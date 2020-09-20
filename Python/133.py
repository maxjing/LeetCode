"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# bfs


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        d = {}
        nodeCopy = Node(node.val, [])
        d[node] = nodeCopy
        q = deque([node])
        while q:
            node = q.popleft()
            for nei in node.neighbors:
                if nei not in d:
                    neiCopy = Node(nei.val, [])
                    d[nei] = neiCopy
                    d[node].neighbors.append(neiCopy)
                    q.append(nei)
                else:
                    d[node].neighbors.append(d[nei])
        return nodeCopy

# dfs


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        self.d = {}
        return self.clone(node)

    def clone(self, node):
        if node.val in self.d:
            return self.d[node.val]
        new_node = Node(node.val, [])
        self.d[node.val] = new_node
        for nei in node.neighbors:
            new_node.neighbors.append(self.clone(nei))
        return new_node
