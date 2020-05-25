class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        store = {}
        store[0] = -1
        s = 0
        for i, num in enumerate(nums):
            s += num
            if k != 0:
                s = s % k
            if s in store:
                if i - store[s] > 1:
                    return True
            else:
                store[s] = i
        return False

'''
[23, 2, 6, 4, 7] 
[23, 7, 7, 5, 12]  each % k = 6
[5, 1, 1, 5, 0] between two 5, beween the two index, there has been added a number which is mutiple of k
{0: -1} is to handle case when [0, 0], 0 
'''
