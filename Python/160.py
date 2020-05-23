# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = headA
        b = headB
        while a != b:
            #2020.05.23 not a.next is None because it will cause infinite loop
            if a is not None:
                a = a.next
            else:
                a = headB
            if b is not None:
                b = b.next
            else:
                b = headA
        return a