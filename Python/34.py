class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = self.searchLeft(nums, target), self.searchRight(nums, target)
        if l <= r:
            return [l, r]
        #target not found
        else:
            return [-1, -1]

    def searchLeft(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l

    def searchRight(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return r