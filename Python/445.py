# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = self.reverse(l1)
        p2 = self.reverse(l2)
        h1, h2 = p1, p2
        dummy = ListNode(-1)
        runner = dummy
        carry = 0
        while h1 or h2:
            a = h1.val if h1 else 0
            b = h2.val if h2 else 0
            digit = (a + b + carry) % 10
            carry = (a + b + carry) // 10
            runner.next = ListNode(digit)
            runner = runner.next
            h1 = h1.next if h1 else None
            h2 = h2.next if h2 else None
        if carry != 0:
            runner.next = ListNode(carry)
        return self.reverse(dummy.next)

    def reverse(self, node):
        if node.next is None:
            return node
        prev = None
        while node is not None:
            next = node.next
            node.next = prev
            prev = node
            node = next
        return prev