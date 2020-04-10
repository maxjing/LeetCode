class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        count = 0
        nums.sort()
        for i in range(len(nums) - 2):
            count += self.searchPair(nums, target - nums[i], i+1)
        return count

    def searchPair(self, nums, target, left):
        count = 0
        right = len(nums) - 1
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum < target:
                count += right - left
                left += 1
            else:
                right -= 1
        return count


'''
Time: 0(nlogn + n^2) 
'''
