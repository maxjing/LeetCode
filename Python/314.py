# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        d = collections.defaultdict(list)
        q = deque([(root, 0)])
        while q:
            node, col = q.popleft()
            d[col].append(node.val)

            if node.left:
                q.append((node.left, col - 1))
            if node.right:
                q.append((node.right, col + 1))
        return [d[i] for i in sorted(d)]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        q = deque([(root, 0)])
        res = defaultdict(list)

        while q:
            level = collections.defaultdict(list)
            for _ in range(len(q)):
                node, col = q.popleft()
                level[col].append(node.val)

                if node.left:
                    q.append((node.left, col - 1))
                if node.right:
                    q.append((node.right, col + 1))

            for col in level:
                #987 sorted(level[col])
                res[col].extend(level[col])

        return [res[i] for i in sorted(res)]