class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        minDiff = math.inf
        nums.sort()
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                currentSum = nums[i] + nums[l] + nums[r]
                currentDiff = target - currentSum
                if currentDiff == 0:
                    return target
                if abs(currentDiff) < abs(minDiff):
                    minDiff = currentDiff
                elif currentDiff > 0:
                    l += 1
                else:
                    r -= 1
        return target - minDiff
