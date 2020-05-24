# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = curr = ListNode(-1)
        dummy.next = head
        while curr.next and curr.next.next:
            first = curr.next
            second = curr.next.next
            first.next = second.next
            second.next = first
            curr.next = second
            curr = first
        return dummy.next
'''
https://leetcode.com/problems/swap-nodes-in-pairs/discuss/11046/My-simple-JAVA-solution-for-share
'''

#2020.05.23 similar to 25 just change k = 2
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = cur = ListNode(-1)
        dummy.next = l = r = head
        while True:
            count = 0
            while r and count < 2:
                r = r.next
                count += 1
            if count == 2:
                prev, curr = r, l
                for _ in range(2):
                    next = curr.next
                    curr.next = prev
                    prev = curr
                    curr = next
                cur.next = prev
                cur = l
                l = r
            else:
                return dummy.next


