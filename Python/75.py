class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, high = 0, len(nums) - 1
        i = 0
        while i <= high:
            if nums[i] == 0:
                nums[i], nums[low] = nums[low], nums[i]
                low += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1


'''
initial: low = 0, high = 4, i = 0, a = [1, 0, 2, 1, 0]
1. a[0] = 1 ->  i = 1, low = 0, high = 4, a = [1, 0, 2, 1, 0] 
2. a[1] = 0 ->  a[1] = arr[0] = 1, a[0] = 0, i = 2, low = 1, high =4, a[0, 1, 2, 1, 0]
3. a[2] = 2 -> a[2] = a[4] = 0, a[4] = 2, low = 1, , high = 3, a[0, 1, 0, 1, 2]
   a[2] = 0 -> a[2] = a[1] = 1, a[1] = 0, i = 3, low = 2, a[0, 0, 1, 1, 2]
4. a[3] = 1
5. i = 4 > high, break
'''
