class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        res = 0
        nums.sort()
        for i in range(len(nums)):
            l, r = 0, i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    res += r - l
                    r -= 1
                else:
                    l += 1
        return res
