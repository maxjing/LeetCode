# xor
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x1 = 0
        for i in range(1, len(nums) + 1):
            x1 = x1 ^ i
        x2 = nums[0]
        for i in range(1, len(nums)):
            x2 = x2 ^ nums[i]

        return x1 ^ x2


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums) + 1):
            sum += i
        for n in nums:
            sum -= n
        return sum


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            j = nums[i]
            if nums[i] < len(nums) and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
