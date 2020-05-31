"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        self.visited = {}
        return self.copy(head)

    def copy(self, node):
        if not node:
            return None
        if node in self.visited:
            return self.visited[node]

        new_node = Node(node.val, None, None)
        self.visited[node] = new_node
        new_node.next = self.copy(node.next)
        new_node.random = self.copy(node.random)

        return new_node
