class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(candidates, target, [], 0, res)
        return res

    def dfs(self, nums, target, sublist, start, res):
        if target < 0:
            return

        if target == 0:
            res.append(sublist)
        #can be repeated use but forward so pass i to dfs
        for i in range(start, len(nums)):
            self.dfs(nums, target - nums[i], sublist + [nums[i]], i, res)


