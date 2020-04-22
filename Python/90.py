# bfs


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        res.append([])
        nums.sort()
        start, end = 0, 0
        for i in range(len(nums)):
            # if current and the previous elements are same, create new subsets only from the subsets added in the previous step
            if i > 0 and nums[i] == nums[i - 1]:
                start = end + 1
            end = len(res) - 1
            for j in range(start, end + 1):
                subList = list(res[j])
                subList.append(nums[i])
                res.append(subList)
        return res

# dfs


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums, res, [], 0)
        return res

    def dfs(self, nums, res, subList, start):
        res.append(list(subList))
        for i in range(start, len(nums)):
            if i != start and nums[i] == nums[i - 1]:
                continue
            subList.append(nums[i])
            self.dfs(nums, res, subList, i + 1)
            subList.pop()
