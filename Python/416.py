class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False

        dp = [False] * (s // 2 + 1)
        dp[0] = True
        for num in nums:
            for i in reversed(range(1, len(dp))):
                if num <= i:
                    dp[i] = dp[i] or dp[i - num]
        return dp[-1]