class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
        # left part in ascending order
            if nums[l] <= nums[mid]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                # in right part
                else:
                    l = mid + 1
        # right part in ascending order
            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                # in left part
                else:
                    r = mid - 1
        return -1
