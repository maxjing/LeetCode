# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        self.res = None
        self.d = defaultdict(list)
        self.leaves = set()
        self.dfs(root)
        self.bfs(k)
        return self.res

    def dfs(self, root):
        if not root:
            return
        if not root.left and not root.right:
            self.leaves.add(root.val)
        if root.left:
            self.d[root.val].append(root.left.val)
            self.d[root.left.val].append(root.val)
            self.dfs(root.left)
        if root.right:
            self.d[root.val].append(root.right.val)
            self.d[root.right.val].append(root.val)
            self.dfs(root.right)

    def bfs(self, k):
        visited = set()
        q = deque()
        q.append(k)
        while q:
            node = q.popleft()
            visited.add(node)
            if node in self.leaves:
                self.res = node
                return
            else:
                for next_node in self.d[node]:
                    if next_node not in visited:
                        q.append(next_node)

'''
dfs build graph paren: children, children: parent
bfs to loop through, the first one found in self.leaves is the answer
'''