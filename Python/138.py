"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
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
        if not head:
            return
        d = {}
        node = head
        while node:
            d[node] = Node(node.val)
            node = node.next

        node = head
        while node:
            # d.get will not throw a exception
            d.get(node).next = d.get(node.next)
            d.get(node).random = d.get(node.random)
            node = node.next

        return d[head]


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
