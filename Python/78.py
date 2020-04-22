# bfs
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        res.append([])
        for n in nums:
            for i in range(len(res)):
                subList = list(res[i])
                subList.append(n)
                res.append(subList)
        return res


'''
iterate the list, put n into all the sublist
[1,2,3]
1. []
2. [], [1]
3. [], [1] + [1, 2], [2]
4. [], [1], [1, 2], [2] + [3], [1, 3], [1, 2, 3], [2, 3]
'''

# dfs


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.dfs(res, [], nums, 0)
        return res

    def dfs(self, res, subList, nums, start):
        res.append(list(subList))
        for i in range(start, len(nums)):
            self.dfs(res, subList + [nums[i]], nums, i + 1)
            # subList.append(nums[i])
            # self.dfs(res, subList, nums, i + 1)
            # subList.pop()


'''
Time: 0(2^N)
'''
