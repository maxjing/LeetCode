# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#bfs
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        if not root:
            return []
        graph = defaultdict(list)

        def dfs(root):
            if not root:
                return
            if root.left:
                graph[root].append(root.left)
                graph[root.left].append(root)
                dfs(root.left)
            if root.right:
                graph[root].append(root.right)
                graph[root.right].append(root)
                dfs(root.right)

        dfs(root)

        visited = set()
        res = []
        q = deque([(target, 0)])
        while q:
            node, k = q.popleft()
            if node in visited:
                continue
            visited.add(node)
            if k == K:
                res.append(node.val)
            elif k < K:
                for next_node in graph[node]:
                    q.append((next_node, k + 1))
        return res


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
