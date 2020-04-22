# dfs
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()
        self.dfs(nums, res, [], visited)
        return res

    def dfs(self, nums, res, subset, visited):
        if len(subset) == len(nums):
            res.append(subset)
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                self.dfs(nums, res, subset+[nums[i]], visited)
                visited.remove(i)
