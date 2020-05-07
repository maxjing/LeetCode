# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        prev, cur = None, head
        for _ in range(m - 1):
            prev = cur
            cur = cur.next
        first_part_last = prev
        second_part_last = cur
        prev = None
        for _ in range(n - m + 1):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        if first_part_last is not None:
            first_part_last.next = prev
        else:
            head = prev
        second_part_last.next = cur
        return head
