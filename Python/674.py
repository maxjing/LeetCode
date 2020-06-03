class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 1
        curr_size = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                curr_size += 1
                res = max(curr_size, res)
            else:
                curr_size = 1
        return res
