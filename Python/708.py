"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        new_node = Node(insertVal, None)
        if not head:
            head = new_node
            head.next = head
            return head
        node = head
        while True:
            if node.next.val > node.val:
                # * next node is increasing
                # * check if insertVal between node vals
                if node.val <= insertVal <= node.next.val:
                    break
            elif node.next.val < node.val:
                # * next node is decreasing
                # * check if insertVal beyond range of cycles
                if insertVal >= node.val or insertVal <= node.next.val:
                    break
            elif node.next == head:
                break
            node = node.next

        new_node.next = node.next
        node.next = new_node
        return head

