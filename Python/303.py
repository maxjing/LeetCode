class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.pre_sum = [0] * len(nums)
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            self.pre_sum[i] = sum

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.pre_sum[j]
        return self.pre_sum[j] - self.pre_sum[i - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)