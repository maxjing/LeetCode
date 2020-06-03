class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1):
            if i % 2 == 1:
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            else:
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = sorted(nums)
        b = sorted(nums, reverse=True)
        j, k = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = a[j]
                j += 1
            else:
                nums[i] = b[k]
                k += 1

