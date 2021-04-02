class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = self.search(nums, target, True), self.search(nums, target, False)
        return [left, right]
    
    def search(self, nums, target, findLeft):
        res = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                res = mid
                if findLeft:
                    r = mid - 1
                else:
                    l = mid + 1
        return res
        
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = self.searchLeft(nums, target), self.searchRight(nums, target)
        return [left, right]
        
    def searchLeft(self, nums, target):
        l, r = 0, len(nums)-1
        res = -1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                res = mid
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return res
    
    def searchRight(self, nums, target):
        l, r = 0, len(nums)-1
        res = -1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                res = mid
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return res