class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for l in range(len(nums)):
            r = len(nums) - 1
            while l < r:
                sum_ = nums[l] + nums[r]
                if sum_ == target:
                    return [l+1, r+1]
                elif sum_ < target:
                    l += 1
                else:
                    r -= 1
        return [-1, -1]
