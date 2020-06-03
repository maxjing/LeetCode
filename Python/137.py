class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        for key, value in d.items():
            if value == 1:
                return key
        return -1