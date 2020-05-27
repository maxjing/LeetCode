class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i == -1:
            return nums.reverse()
        j = len(nums) - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        l, r = i + 1, len(nums) - 1
        #reverse left part, they are descending
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


'''
[1,2,6,4,2]
1. from right to find the first index which is smaller than its right -> 2
    if find none, means already revered, so return reverse
2. from right to find the most close greater number than the number from step1 -> 4
3. switch 2 and 4 -> 14622
4. from step one index i + 1 to last element, reverse -> 14 226
'''