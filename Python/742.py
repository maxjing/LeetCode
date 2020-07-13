# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        leaves = []
        graph = defaultdict(list)

        def dfs(root):
            if not root.left and not root.right:
                leaves.append(root.val)
            if not root:
                return
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                dfs(root.left)
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                dfs(root.right)

        dfs(root)
        q = deque([k])
        visited = set()
        while q:
            node = q.popleft()
            visited.add(node)
            if node in leaves:
                return node
            for next_node in graph[node]:
                if next_node not in visited:
                    q.append(next_node)
        return -1


'''
dfs build graph paren: children, children: parent
bfs to loop through, the first one found in self.leaves is the answer
'''