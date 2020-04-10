class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < len(nums) - 1 and nums[low] <= nums[low + 1]:
            low += 1
        while high > 0 and nums[high] >= nums[high - 1]:
            high -= 1

        if low == len(nums) - 1:
            return 0

        sub_min = math.inf
        sub_max = -math.inf

        for i in range(low, high + 1):
            sub_min = min(sub_min, nums[i])
            sub_max = max(sub_max, nums[i])

        while low > 0 and nums[low - 1] > sub_min:
            low -= 1
        while high < len(nums) - 1 and nums[high + 1] < sub_max:
            high += 1
        return high - low + 1
