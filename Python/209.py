class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        res, l, sum = math.inf, 0, 0
        for r in range(len(nums)):
            sum += nums[r]
            while sum >= s:
                res = min(res, r - l + 1)
                sum -= nums[l]
                l += 1
        return 0 if res == math.inf else res