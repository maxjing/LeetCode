class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if n <= 11:
            return -1
        nums = list(map(int, str(n)))
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i == -1:
            return -1
        j = len(nums) - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        i, j = i + 1, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        res = int("".join(map(str, nums)))
        return res if res < 2 ** 31 else -1


