class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.dfs(candidates, target, [], 0, res)
        return res

    def dfs(self, nums, target, sublist, start, res):
        if target < 0:
            return
        if target == 0:
            res.append(sublist)

        for i in range(start, len(nums)):
            if (i > start and nums[i] == nums[i - 1]):
                continue

            self.dfs(nums, target - nums[i], sublist + [nums[i]], i + 1, res)
