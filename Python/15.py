class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.searchPair(nums, -nums[i], i + 1, res)
        return res

    def searchPair(self, nums, target, left, res):
        right = len(nums) - 1
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                res.append([-target, nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1


'''
Time: O(nlogn + n^2)
sort is nlogn, while loop inside while loop is n^2

Space: O(n) for sorting
'''
