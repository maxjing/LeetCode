# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        def dfs(nums):
            if not nums:
                return
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = dfs(nums[:mid])
            root.right = dfs(nums[mid+1:])
            return root
        return dfs(nums)


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        return self.dfs(nums, 0, len(nums) - 1)

    def dfs(self, nums, l, r):
        if l > r:
            return None
        mid = l + (r - l) // 2
        root = TreeNode(nums[mid])
        root.left = self.dfs(nums, l, mid - 1)
        root.right = self.dfs(nums, mid + 1, r)
        return root