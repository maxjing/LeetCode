class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            # remember to check nums[i] also
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                currentSum = nums[i] + nums[l] + nums[r]
                if currentSum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif currentSum > 0:
                    r -= 1
                else:
                    l += 1
        return res


'''
Time: O(nlogn + n^2)
sort is nlogn, while loop inside while loop is n^2

Space: O(n) for sorting
'''
