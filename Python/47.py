class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        visited = [False for x in range(len(nums))]
        res = []
        self.dfs(nums, [], visited, res)
        return res

    def dfs(self, nums, sublist, visited, res):
        if len(sublist) == len(nums):
            res.append(sublist)
        for i in range(len(nums)):
            if not visited[i]:
                if i > 0 and not visited[i - 1] and nums[i] == nums[i - 1]:
                    continue
                visited[i] = True
                self.dfs(nums, sublist + [nums[i]], visited, res)
                visited[i] = False