class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums

    def pick(self, target: int) -> int:

        seen = 0
        for i in range(len(self.arr)):
            if self.arr[i] == target:
                seen += 1
                pick = random.randint(1, seen)
                #pick == seen also works
                if pick == 1:
                    res = i
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)