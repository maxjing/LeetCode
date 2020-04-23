class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if nums[l] <= nums[r]:
            return nums[l]
        while l < r:  # or l <= r
            mid = l + (r - l) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] < nums[mid - 1]:
                return nums[mid]
            # search right part
            elif nums[l] <= nums[mid]:
                l = mid + 1
            # search left part
            else:
                r = mid - 1
        return -1
