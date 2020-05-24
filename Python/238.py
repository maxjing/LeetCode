class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = 1, 1
        res = [0] * len(nums)
        for i in range(len(nums)):
            if i != 0:
                left *= nums[i - 1]
            res[i] = left

        for i in range(len(nums) - 1, -1, -1):
            if i != len(nums) - 1:
                right *= nums[i + 1]
            res[i] *= right
        return res

'''
[1, 2, 3, 4] first iterate [1, 1, 2, 6]
'''