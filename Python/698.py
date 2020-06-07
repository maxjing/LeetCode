class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k is not 0:
            return False
        if k <= 0 or total % k is not 0:
            return False
        return self.dfs(nums, k, 0, 0, total // k, set())

    def dfs(self, nums, k, start, curr_sum, target, seen):
        if k == 1:
            return True
        if curr_sum > target:
            return False

        if curr_sum == target:
            return self.dfs(nums, k - 1, 0, 0, target, seen)
        for i in range(start, len(nums)):
            if i not in seen:
                seen.add(i)
                if self.dfs(nums, k, i + 1, curr_sum + nums[i], target, seen):
                    return True
                seen.remove(i)
        return False