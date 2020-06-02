#dp with memorization
class Solution:
    def findTargetSumWays(self, nums, S):
        curr_sum = 0
        self.memo = {}
        return self.dp(nums, S, 0, curr_sum)

    def dp(self, nums, target, index, curr_sum):
        if (curr_sum, index) in self.memo:
            return self.memo[(curr_sum, index)]
        if index == len(nums) and curr_sum == target:
            return 1
        if index == len(nums):
            return 0

        positive = self.dp(nums, target, index + 1, curr_sum + nums[index])
        negative = self.dp(nums, target, index + 1, curr_sum + -nums[index])

        self.memo[(curr_sum, index)] = positive + negative
        return self.memo[(curr_sum, index)]

#without memorization
class Solution:
    def findTargetSumWays(self, nums, S):
        curr_sum = 0
        return self.dp(nums, S, 0, curr_sum)

    def dp(self, nums, target, index, curr_sum):
        if index == len(nums) and curr_sum == target:
            return 1
        if index == len(nums):
            return 0

        positive = self.dp(nums, target, index + 1, curr_sum + nums[index])
        negative = self.dp(nums, target, index + 1, curr_sum + -nums[index])

        return positive + negative


#my own solution, tle leetcode, need memorization
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.res = 0
        self.dfs(nums, '', 0, S)
        return self.res

    def dfs(self, nums, path, pos, target):
        if pos == len(nums):
            if target == 0:
                self.res += 1
            return

        self.dfs(nums, path + '+' + str(nums[pos]), pos + 1, target - nums[pos])
        self.dfs(nums, path + '-' + str(nums[pos]), pos + 1, target + nums[pos])
