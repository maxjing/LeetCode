class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, start, curr, res):
        if len(curr) >= 2:
            res.append(curr)
        used = set()
        for i in range(start, len(nums)):
            if nums[i] in used or (len(curr) > 0 and curr[-1] > nums[i]):
                continue
            used.add(nums[i])
            self.dfs(nums, i + 1, curr + [nums[i]], res)

