class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            if nums[abs(n) - 1] < 0:
                res.append(abs(n))
            else:
                nums[abs(n) - 1] *= -1
        return res

'''
所有的数都是positive的，遇到第一次 设置成-1， 第二次再遇到这个数 它一定是负数
'''