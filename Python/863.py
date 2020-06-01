# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#bfs
class Solution:
    def buildGraph(self, node, parent, graph):
        if not node:
            return
        if parent:
            graph[node].append(parent)
        if node.left:
            graph[node].append(node.left)
            self.buildGraph(node.left, node, graph)
        if node.right:
            graph[node].append(node.right)
            self.buildGraph(node.right, node, graph)

    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        graph = defaultdict(list)
        self.buildGraph(root, None, graph)
        q = deque([(target, 0)])
        visited = set()
        res = []
        while q:
            node, distance = q.popleft()
            if node in visited:
                continue
            visited.add(node)
            if distance == K:
                res.append(node.val)
            elif distance < K:
                for child in graph[node]:
                    q.append((child, distance + 1))
        return res

'''
dfs only build node -> parent graph
'''
class Solution:

    def buildGraph(self, node, parent, graph):
        if not node:
            return
        graph[node] = parent
        self.buildGraph(node.left, node, graph)
        self.buildGraph(node.right, node, graph)

    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        graph = {}
        self.buildGraph(root, None, graph)
        visited = set()
        res = []

        def dfs(node, distance):
            if not node or node in visited:
                return
            visited.add(node)
            if distance == K:
                res.append(node.val)
            elif distance < K:
                dfs(node.left, distance + 1)
                dfs(node.right, distance + 1)
                dfs(graph[node], distance + 1)

        dfs(target, 0)
        return res
