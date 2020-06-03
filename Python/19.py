# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        h1, h2 = head, head
        while n > 0:
            h2 = h2.next
            n -= 1
        if not h2:
            return head.next
        #2020.06.03 h1 need stay one ahead
        h2 = h2.next
        while h2:
            h1 = h1.next
            h2 = h2.next
        h1.next = h1.next.next
        return head

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n == 0:
            return head
        reversed_head = self.reverse(head)
        curr = reversed_head
        if n == 1:
            return self.reverse(curr.next)
        count = 0
        while count < n - 2:
            curr = curr.next
            count += 1
        curr.next = curr.next.next
        return self.reverse(reversed_head)

    def reverse(self, node):
        prev = None
        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next
        return prev
