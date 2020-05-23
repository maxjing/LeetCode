# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        head = node = self.reverse(head)
        while node.val == 9:
            node.val = 0
            if not node.next:
                node.next = ListNode(0)
            node = node.next
        node.val += 1
        return self.reverse(head)

    def reverse(self, node):
        prev = None
        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next
        return prev

#2020.05.23 my own solution
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        cur = dummy
        reversed = self.reverse(head)
        digit = (reversed.val + 1) % 10
        carry = (reversed.val + 1) // 10
        cur.next = ListNode(digit)
        cur = cur.next
        reversed = reversed.next
        while reversed:
            sum = reversed.val + carry
            cur.next = ListNode(sum % 10)
            carry = sum // 10
            cur = cur.next
            reversed = reversed.next
        if carry != 0:
            cur.next = ListNode(carry)
        return self.reverse(dummy.next)

    def reverse(self, node):
        prev = None
        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next
        return prev

'''
compared with the first solution, no need extra space and only care the digit is 9
there is only one digit need to plus one 9 -> 9 -> 9 : 0 -> 0 -> 0 -> 1
'''