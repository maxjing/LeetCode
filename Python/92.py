# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        prev, current = None, head
        i = 0
        while current is not None and i < m - 1:
            prev = current
            current = current.next
            i += 1

        last_node_of_first_part = prev
        last_node_of_sublist = current

        i = 0
        prev = None
        while current is not None and i < n - m + 1:
            next = current.next
            current.next = prev
            prev = current
            current = next
            i += 1
        # m is not 1
        if last_node_of_first_part is not None:
            last_node_of_first_part.next = prev
        else:
            head = prev
        last_node_of_sublist.next = current

        return head
