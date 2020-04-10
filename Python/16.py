class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        smallest_diff = math.inf
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                current_diff = target - current_sum
                if current_diff == 0:
                    return target
                if (abs(smallest_diff) > abs(current_diff)) or (abs(smallest_diff) == abs(current_diff) and current_diff > smallest_diff):
                    smallest_diff = current_diff
                if current_diff > 0:
                    left += 1
                else:
                    right -= 1
        return target - smallest_diff
